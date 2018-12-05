#!/usr/bin/env python
# -*- encoding: utf-8

import os
import traceback

import click
import tqdm

from sinkingship import find_all_metadata_files, save_post_media_files


@click.command(
    help="Save all the media files for your Tumblr posts/likes."
)
@click.option(
    "--metadata", default="tumblr",
    help="Directory where your metadata is saved."
)
def save_all_media_files(metadata):
    all_media_files = list(find_all_metadata_files(path=metadata))
    for info_path in tqdm.tqdm(all_media_files):
        try:
            save_post_media_files(info_path)
        except Exception:
            post_id = os.path.basename(os.path.dirname(info_path))
            traceback.print_exc()
            print(f"Error trying to save post {post_id}!!")
            print("~")


if __name__ == '__main__':
    save_all_media_files()
