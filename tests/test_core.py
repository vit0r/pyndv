"""Tests for core FeedProcessor
"""
from datetime import datetime

import pytest

from pyndv import core


@pytest.mark.parametrize('feed_type', ['modified'])
def test_feed_processor_modified_feed_success(feed_type):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed_type, output='test_file.json')
    assert isinstance(feed_processor.feed_json, dict)
    assert feed_processor.feed_resource_url == 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-modified.json.gz'


@pytest.mark.parametrize('feed_type', ['recent'])
def test_feed_processor_recent_feed_success(feed_type):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed_type, output='test_file.json')
    assert feed_processor.feed_resource_url == 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-recent.json.gz'


@pytest.mark.parametrize('feed_type', ['none'])
@pytest.mark.parametrize('year', [datetime.now().year])
def test_feed_processor_invalid_feed_get_default_year_success(feed_type, year):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed_type, output='test_file.json')
    assert feed_processor.feed_resource_url == 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-{}.json.gz'.format(
        year)
