"""Tests for core FeedProcessor
"""
import os
from datetime import datetime
from pathlib import Path

import pytest

from pyndv import core


@pytest.mark.parametrize("feed_type", ["modified"])
def test_feed_processor_modified_feed_success(feed_type, feed_url_modified):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed_type)
    assert isinstance(feed_processor.feed_json, dict)
    assert feed_processor.feed_resource_url == feed_url_modified


@pytest.mark.parametrize("feed_type", ["recent"])
def test_feed_processor_recent_feed_success(feed_type, feed_url_recent):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed_type)
    assert feed_processor.feed_resource_url == feed_url_recent


@pytest.mark.parametrize("year", [datetime.now().year])
def test_feed_processor_invalid_feed_get_default_year_success(year, feed_url_year):
    feed_processor = core.FeedProcessor()
    feed_processor()
    assert feed_processor.feed_resource_url == feed_url_year


@pytest.mark.parametrize("output_file", ["test_file.json"])
def test_feed_processor_with_output_file(output_file):
    feed_processor = core.FeedProcessor()
    feed_processor(output=output_file)
    file_path = Path(output_file)
    assert file_path.exists()
    os.remove(str(file_path.resolve()))
