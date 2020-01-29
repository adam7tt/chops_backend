#!/usr/bin/env python3

from typing import Union, Sequence
from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import Schema
from chops.flask_extensions import db
from chops.database.models import Academic

blueprint = Blueprint('academics', __name__)

academic_args = {
        'id': fields.Integer(),
        'ids': fields.DelimitedList(fields.Integer(), delimiter=','),
        'name': fields.Str(),
        'department': fields.Str(),
        'university': fields.Str()
        }

@blueprint.route('/', methods=['GET', 'POST'])
@use_args(academic_args)
def get_academic(args):
    ret = None
    if 'id' in args:
        ret = Academic.query.filter_by(id=args['id']).first()
    return jsonify(ret)

