#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
import logging
import argparse
from pathlib import Path
from flask import Flask

from chops.core.flask_extensions import db
from chops.controllers import (academics, citations)

def create_api(config_object='chops.core.settings'):
    # name = '.'.join(__name__.split('.')[:-1])
    # name = sys.path.append(str(Path(__file__).absolute()))
    name = __name__
    # print(name, type(name))
    api = Flask(name)
    api.config.from_object(config_object)
    register_extensions(api)
    register_blueprints(api)
    configure_logger(api)
    return api

def register_extensions(api):
    db.init_app(api)
    return None

def register_blueprints(api):
    api.register_blueprint(academics.blueprint, url_prefix='/academics')
    api.register_blueprint(citations.blueprint, url_prefix='/citations')
    return None

def configure_logger(api):
    handler = logging.StreamHandler(sys.stdout)
    if not api.logger.handlers:
        api.logger.addHandler(handler)
    return None

def get_args():
    """Define and handle command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', dest='debug', action='store_const', const='development', default='production', help='debug mode (default: off)')
    return parser.parse_args()

args = get_args()
os.environ['FLASK_ENV'] = args.debug
api = create_api()
api.run()