"""Tests for subprocess client
"""
import subprocess

import pytest


@pytest.mark.parametrize("feed_type", ["modified"])
@pytest.mark.parametrize("file_name", ["file_test.json"])
def test_subprocess_modified_feed_success(feed_type, file_name, capfd):
    subprocess.call(
        ["python", "-m", "pyndv", "-f", feed_type, "-o", file_name], shell=True
    )
    *_, err = capfd.readouterr()
    assert not err


@pytest.mark.parametrize("feed_type", ["recent"])
@pytest.mark.parametrize("file_name", ["file_test.json"])
def test_subprocess_recent_feed_success(feed_type, file_name, capfd):
    subprocess.call(
        ["python", "-m", "pyndv", "-f", feed_type, "-o", file_name], shell=True
    )
    *_, err = capfd.readouterr()
    assert not err


@pytest.mark.parametrize("feed_type", ["none"])
def test_subprocess_invalid_feed_get_default_year_success(feed_type, capfd):
    subprocess.call(["python", "-m", "pyndv", "-f", feed_type], shell=True)
    *_, err = capfd.readouterr()
    assert not err
