""" tests configurations

Module to configure pytest before run

Returns:
    [fixture]: global fixtures autouse
"""

from datetime import datetime

import pytest


@pytest.fixture(autouse=True, scope="session")
def feed_url_modified():
    """feed_url_modified return str url for feed modified

    Fixture returns url feed modified

    Returns:
        [str]: url for feed modified
    """
    return "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.gz"


@pytest.fixture(autouse=True, scope="session")
def feed_url_recent():
    """feed_url_recent return str url for feed recent

    Fixture returns url feed recent

    Returns:
        [str]: url for feed recent
    """
    return "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-recent.json.gz"


@pytest.fixture(autouse=True, scope="session")
def feed_url_year():
    """feed_url_year return str url for feed year

    Fixture returns url feed year

    Returns:
        [str]: url for feed year
    """
    return "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{}.json.gz".format(
        datetime.now().year
    )
