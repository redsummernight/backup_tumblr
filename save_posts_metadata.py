#!/usr/bin/env python
# -*- encoding: utf-8

import os

import click

from garbagesite import get_all_posts, save_post_metadata


@click.command(
    help="Save all the metadata from your Tumblr posts."
)
@click.option(
    "--blog_identifier", required=True,
    default="redsummernight.tumblr.com",
    prompt="What is your blog identifier? e.g. 'alexwlchan.tumblr.com'",
    help="Blog identifier, as used by the Tumblr API"
)
@click.option(
    "--api_key", required=True,
    prompt="What is your API key? Register at https://www.tumblr.com/oauth/apps",
    help="OAuth API key for the Tumblr API (https://www.tumblr.com/oauth/apps)"
)
@click.option(
    "--dst", default="tumblr",
    help="Directory for saving metadata"
)
def save_metadata(blog_identifier, api_key, dst):
    for post_data in get_all_posts(blog_identifier=blog_identifier, api_key=api_key):
        save_post_metadata(
            dst=os.path.join(dst, blog_identifier.replace(".", "_"), "posts"),
            post_data=post_data
        )

if __name__ == '__main__':
    save_metadata()
    print(
        "Note: if the progress bar didn't quite get to 100%, that's okay -- "
        "it's only an estimate, and the Tumblr API doesn't always return everything."
    )
