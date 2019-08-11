"""Tests for subprocess client
"""
import subprocess
from datetime import datetime

import pytest


@pytest.mark.parametrize('feed_type', ['modified'])
def test_subprocess_modified_feed_success(feed_type, capfd):
    subprocess.call(['python', '-m', 'pyndv', '-f', feed_type], shell=True)
    out, err = capfd.readouterr()
    assert not err


@pytest.mark.parametrize('feed_type', ['recent'])
def test_subprocess_recent_feed_success(feed_type, capfd):
    subprocess.call(['python', '-m', 'pyndv', '-f', feed_type], shell=True)
    out, err = capfd.readouterr()
    assert not err


@pytest.mark.parametrize('feed_type', ['none'])
def test_subprocess_invalid_feed_get_default_year_success(feed_type, capfd):
    subprocess.call(['python', '-m', 'pyndv', '-f', feed_type], shell=True)
    out, err = capfd.readouterr()
    assert not err
