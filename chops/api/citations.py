#!/usr/bin/env python3

from typing import Union, Sequence
from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import Schema
from chops.flask_extensions import db
from chops.database.models import (Citation, Academic, Keyword)

blueprint = Blueprint('citations', __name__)

citation_args = {
        'id': fields.Integer(),
        'ids': fields.DelimitedList(fields.Integer(), delimiter=','),
        'keywords': fields.DelimitedList(fields.Integer(), delimiter=','),
        # 'academics_id': fields.DelimitedList(fields.Integer(), delimiter=','),
        'academic_id': fields.Integer(),
        'search': fields.Str()
        }

@blueprint.route('/', methods=['GET', 'POST'])
@use_args(citation_args)
def get_academic(args):
    ret = []
    if 'id' in args:
        ret = Citation.query.filter_by(id=args['id']).first()
        return jsonify(ret())
    elif 'ids' in args:
        ret = db.session.query(Citation).filter(Citation.id.in_(args['ids'])).all()
        return jsonify([r() for r in ret])
    elif 'academic_id' in args:
        ret = db.session.query(Citation).join(Citation.academics).filter(Academic.id == args['academic_id'])
        return jsonify([r() for r in ret])
    elif 'search' in args:
        ret = db.session.query(Citation) \
            .join(Citation.keywords) \
            .filter(Citation.title.contains(args['search'])) \
            .filter(Keyword.name.contains(args['search'])) \
            .all()
        return jsonify([r() for r in ret])
    else:
        ret = db.session.query(Citation).all()
        return jsonify([r() for r in ret])