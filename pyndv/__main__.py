#!/usr/bin/env python3
"""
Cli to process feed_json to dict
"""
import click

from pyndv import core


@click.command(name=__name__)
@click.option(
    "--feed", "-f", default="recent", help="Feed name", prompt="Selected feed: "
)
@click.option(
    "--output",
    "-o",
    default="pyndv_output.json",
    help="output file name",
    prompt="Output file name: ",
    required=True,
)
def main(feed=None, output=None):
    """ Main entry point of the app """
    feed_processor = core.FeedProcessor()
    feed_processor(feed_type=feed, output=output)
    return feed_processor.feed_json


if __name__ == "__main__":
    main()
