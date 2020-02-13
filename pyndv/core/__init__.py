"""Download feeds JSON from https://nvd.nist.gov/feeds/json/cve/1.0
"""
import gzip
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

import requests


class FeedProcessor:
    """Process feed"""

    _FEED_JSON_URL = "https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-{}.json.gz"

    def _init_(self):
        """Init self"""
        self._feed_json = None
        self._feed_resource_url = None
        self._feed_type = None
        self._output_file = None

    def __repr__(self):
        """Representation of class"""
        return "{}()".format(self.__class__.__name__)

    def __call__(self, *args, **kwargs):
        """get feed json by type"""
        self._setdefault_feed_type(kwargs)
        self._output_file = kwargs.get("output")
        self._download_feed_resource()

    @property
    def feed_json(self):
        """Feed json data"""
        return self._feed_json

    @property
    def feed_resource_url(self):
        """Feed type url"""
        return self._feed_resource_url

    def _process_feed(self, process):
        response = process.result()
        if response.status_code != 200:
            raise ValueError("Error to request feed url")
        nvdcve_json_str = gzip.decompress(response.content)
        self._feed_json = json.loads(nvdcve_json_str)
        self._write_output_file()

    def _download_feed_resource(self):
        """Download feed resource by feed type"""
        self._feed_resource_url = self._FEED_JSON_URL.format(self._feed_type)
        with ThreadPoolExecutor(max_workers=1) as processor:
            process = processor.submit(
                requests.get, self._feed_resource_url, stream=True
            )
            print("Start download {}".format(self._feed_type))
            while process.running():
                print(".", end="")
            if process.done():
                print("Download complete.")
            process.add_done_callback(self._process_feed)

    def _setdefault_feed_type(self, kwargs):
        """Set default value if feed type not exists"""
        self._feed_type = kwargs.get("feed_type", None)
        current_year = datetime.now().year
        if self._feed_type not in ["recent", "modified", current_year]:
            self._feed_type = current_year

    def _write_output_file(self):
        assert self._output_file, "output file needed"
        output_file_path = Path(self._output_file)
        if output_file_path.exists():
            new_file_name = "{}.json".format(datetime.utcnow().time())
            output_file_path = Path(output_file_path.parent, new_file_name)
        data_str = json.dumps(self._feed_json, sort_keys=False, indent=2)
        output_file_path.write_text(data_str)
