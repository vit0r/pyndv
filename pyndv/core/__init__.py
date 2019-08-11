"""Download feeds JSON from https://nvd.nist.gov/feeds/json/cve/1.0
"""
import gzip
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import requests


class FeedProcessor:
    """Process feed"""

    __FEED_JSON_URL = 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-{}.json.gz'

    def __init__(self):
        """Init self"""
        self.__feed_json = None
        self.__feed_resource_url = None
        self.__feed_type = None
        self.year = datetime.now().year

    def __repr__(self):
        """Representation of class"""
        return '{}()'.format(self.__class__.__name__)

    @property
    def feed_json(self):
        """Feed json data"""
        return self.__feed_json

    @property
    def feed_resource_url(self):
        """Feed type url"""
        return self.__feed_resource_url

    def __process_feed(self, process):
        response = process.result()
        if response.status_code != 200:
            raise ValueError('Error to request feed url')
        nvdcve_json_str = gzip.decompress(response.content)
        self.__feed_json = json.loads(nvdcve_json_str)

    def __download_feed_resource(self):
        """Download feed resource by feed type"""
        self.__feed_resource_url = self.__FEED_JSON_URL.format(
            self.__feed_type)
        with ThreadPoolExecutor(max_workers=1) as processor:
            process = processor.submit(
                requests.get, self.__feed_resource_url, stream=True)
            print('Start download {}'.format(self.__feed_type))
            while process.running():
                print('.', end='')
            if process.done():
                print('Download complete.')
            process.add_done_callback(self.__process_feed)

    def __call__(self, *args, **kwargs):
        """get feed json by type"""
        self.__setdefault_feed_type(kwargs)
        self.__download_feed_resource()

    def __setdefault_feed_type(self, kwargs):
        """Set default value if feed type not exists"""
        self.__feed_type = kwargs.get('feed_type', None)
        if self.__feed_type not in ['recent', 'modified', self.year]:
            self.__feed_type = self.year
