#!/usr/bin/env python3
"""
Cli to process feed_json to dict
"""
from datetime import datetime

import click

from pyndv import core


@click.command(name=__name__)
@click.option(
    "--feed",
    "-f",
    type=click.Choice(
        ["recent", "modified", str(datetime.now().year)], case_sensitive=True
    ),
    default=str(datetime.now().year),
    help="Feed name",
)
@click.option("--output", "-o", type=str, help="output")
@click.option("--verbose", "-d", type=bool, help="verbose", default=True)
@click.help_option()
def main(feed, output, verbose):
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed, output=output, verbose=verbose)
    return feed_processor.feed_json


if __name__ == "__main__":
    main()
