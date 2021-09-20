"""Download feeds JSON
"""

import gzip
import json
import logging
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

import requests

FEED_JSON_URL = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{}.json.gz"


class FeedProcessor:
    def _init_(self):
        self._feed_json = None
        self._feed_resource_url = None
        self._feed_type = None
        self._output_file = None

    def __repr__(self):
        return "{}()".format(self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        self._feed_type = kwargs.get("feed_type", datetime.now().year)
        self._output_file = kwargs.get("output")
        self._verbose = kwargs.get("verbose")
        self._download_feed_resource()

    @property
    def feed_json(self):
        return self._feed_json

    @property
    def feed_resource_url(self):
        return self._feed_resource_url

    def _process_feed(self, process):
        response = process.result()
        if response.status_code != 200:
            raise ValueError("feed", self.feed_resource_url)
        nvdcve_json_str = gzip.decompress(response.content)
        self._feed_json = json.loads(nvdcve_json_str)
        if self._output_file:
            self._write_output_file()

    def _download_feed_resource(self):
        self._feed_resource_url = FEED_JSON_URL.format(self._feed_type)
        with ProcessPoolExecutor(max_workers=2) as processor:
            process = processor.submit(
                requests.get, self._feed_resource_url, stream=True
            )
            if self._verbose:
                logging.info("Download started.")
                while process.running():
                    if process.done():
                        logging.info("Download complete.")
            process.add_done_callback(self._process_feed)

    def _write_output_file(self, sort_keys=False, indent=2):
        with Path(self._output_file).open(mode="w+") as output_file:
            output_file.truncate()
            data_str = json.dumps(self._feed_json, sort_keys=sort_keys, indent=indent)
            output_file.write(data_str)
