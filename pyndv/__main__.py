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
    type=click.Option(["recent", "modified", datetime.now().year]),
    default="recent",
    help="Feed name",
    prompt="Selected feed: ",
)
@click.option(
    "--output",
    "-o",
    type=click.types.STRING,
    help="output file name",
    prompt="Output file name: ",
)
@click.version_option()
def main(feed, output):
    """main [summary]
    
    [extended_summary]
    
    Args:
        feed ([type], optional): [description]. Defaults to str.
        output ([type], optional): [description]. Defaults to File.
    
    Returns:
        [type]: [description]
    """
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed, output=output)
    return feed_processor.feed_json


if __name__ == "__main__":
    main()
