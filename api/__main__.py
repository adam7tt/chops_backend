#!/usr/bin/env python3

import argparse
import logging
from flask import Flask

logger = logging.getLogger(__name__)
api = Flask(__name__)

def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', dest='debug', action='store_const',
                        const=True, default=False, help='verbose mode (default: off)')

    return parser.parse_args()


def main():
    """Starts api using command line args"""

    args = get_args()

    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if args.debug else logging.WARNING)

    api.run(debug=args.debug)


if __name__ == '__main__':
    main()
