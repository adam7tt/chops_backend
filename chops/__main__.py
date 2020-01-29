#!/usr/bin/env python3

import os
import argparse
from flask import Flask

from .api.api import create_api

def get_args():
    """Define and handle command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', dest='debug', action='store_const',
                        const='development', default='production', help='debug mode (default: off)')

    return parser.parse_args()


def main():
    """Starts api setting the environment using command line args"""

    args = get_args()
    os.environ['FLASK_ENV'] = args.debug
    api = create_api()
    api.run()


if __name__ == '__main__':
    main()
