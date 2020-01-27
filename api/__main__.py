#!/usr/bin/env python3
import sys, os
import argparse
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent)

connection = {
   'name': 'chops',
   'user': 'admin',
   'pw': 'Redandgreenchristmaspajamas',
   'host': 'db-chops.ca4hnifnf4lg.us-west-1.rds.amazonaws.com',
   'port': 3306,
}

logger = logging.getLogger(__name__)
api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(connection['user'], connection['pw'], connection['host'], connection['dbname'])
db = SQLAlchemy(api)

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
