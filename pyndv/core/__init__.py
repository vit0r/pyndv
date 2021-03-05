"""Download feeds JSON from https://nvd.nist.gov/feeds/json/cve/1.0
"""

import gzip
import json
import timeit
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

import requests


class FeedProcessor:
    """Feed Processor class
    Manipulate process to download and produce file/stream json with feed data

    Raises:
        ValueError: Error when download feed .gz

    Returns:
        [type]: feed type
    """

    _FEED_JSON_URL = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{}.json.gz"

    def _init_(self):
        """_init_ [summary]

        [extended_summary]
        """
        self._feed_json = None
        self._feed_resource_url = None
        self._feed_type = None
        self._output_file = None

    def __repr__(self):
        """__repr__ [summary]

        [extended_summary]

        Returns:
            [type]: [description]
        """
        return "{}()".format(self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        """__call__ [summary]

        [extended_summary]
        """
        self._feed_type = kwargs.get("feed_type", datetime.now().year)
        self._output_file = kwargs.get("output")
        self._download_feed_resource()

    @property
    def feed_json(self):
        """feed_json data feed json

        Feed data json was dictionary

        Returns:
            [dict]: json dict
        """
        return self._feed_json

    @property
    def feed_resource_url(self):
        """feed_resource_url feed url

        Store value for resource url

        Returns:
            [str]: download url for feed
        """
        return self._feed_resource_url

    def _process_feed(self, process):
        """_process_feed run process to download and create file if output was passed
        Start process thread pool executor

        Args:
            process (ProcessExecutor): Process executor

        Raises:
            ValueError: When download fails
        """
        response = process.result()
        if response.status_code != 200:
            raise ValueError("Error to request feed url >> ", self.feed_resource_url)
        nvdcve_json_str = gzip.decompress(response.content)
        self._feed_json = json.loads(nvdcve_json_str)
        if self._output_file:
            self._write_output_file()

    def _download_feed_resource(self, verbose=False):
        """_download_feed_resource download feed process
        Download feed from nvde site https://nvd.nist.gov/feeds/json/cve/1.1
        """
        self._feed_resource_url = self._FEED_JSON_URL.format(self._feed_type)
        with ProcessPoolExecutor(max_workers=1) as processor:
            process = processor.submit(
                requests.get, self._feed_resource_url, stream=True
            )
            if verbose:
                print("Starting download >> ", timeit.default_timer())
                while process.running():
                    print("Downloading >> ", timeit.default_timer())
                if process.done():
                    print("Download complete >> ", timeit.default_timer())
            process.add_done_callback(self._process_feed)

    def _write_output_file(self, sort_keys=False, indent=2):
        """_write_output_file create file .json on disk

        Create output file json data on disk

        Args:
            sort_keys (bool, optional): organize keys on json. Defaults to False.
            indent (int, optional): indent space file json with. Defaults to 2.
        """
        with Path(self._output_file).open(mode="w+") as output_file:
            output_file.truncate()
            data_str = json.dumps(self._feed_json, sort_keys=sort_keys, indent=indent)
            output_file.write(data_str)
