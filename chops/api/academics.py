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
        'university': fields.Str(),
        'search': fields.Str()
        }

@blueprint.route('/', methods=['GET', 'POST'])
@use_args(academic_args)
def get_academic(args):
    ret = []
    if 'search' in args:
        ret = db.session.query(Academic)\
            .filter(Academic.name.contains(args['search']))\
            .filter(Academic.university.contains(args['search']))\
            .all()
        return jsonify([r.json() for r in ret])
    if 'id' in args:
        ret = Academic.query.filter_by(id=args['id']).first()
        return jsonify(ret.json())
    if 'ids' in args:
        ret = db.session.query(Academic).filter(Academic.id.in_(args['ids'])).all()
        return jsonify([r.json() for r in ret])
    if 'name' in args:
        # ret = Academic.query.filter_by(name=args['name']).all()
        ret = db.session.query(Academic).filter(Academic.name.contains(args['name'])).all()
        return jsonify([r.json() for r in ret])
