#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

connection = {
        'NAME': 'chops',
        'USER': 'admin',
        'PASSWORD': 'Redandgreenchristmaspajamas',
        'HOST': 'db-chops.ca4hnifnf4lg.us-west-1.rds.amazonaws.com',
        'PORT': 3306
        }

default_database_uri = 'mysql+mysqldb://{}:{}@{}/{}'.format(connection['USER'], connection['PASSWORD'],
                                                            connection['HOST'], connection['NAME'])

ENV = os.getenv('FLASK_ENV', 'production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', None) or default_database_uri
SECRET_KEY = os.getenv('SECRET_KEY', None) or connection['PASSWORD']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SEND_FILE_MAX_AGE_DEFAULT = os.getenv("SEND_FILE_MAX_AGE_DEFAULT")
if SEND_FILE_MAX_AGE_DEFAULT:
    SEND_FILE_MAX_AGE_DEFAULT = int(SEND_FILE_MAX_AGE_DEFAULT)
