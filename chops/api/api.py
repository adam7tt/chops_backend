#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging

from flask import Flask

from chops.flask_extensions import db
from chops.api import (academics, citations)

def create_api(config_object='chops.settings'):
    api = Flask('.'.join(__name__.split('.')[:-1]))
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
