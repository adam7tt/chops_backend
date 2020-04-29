#!/usr/bin/env python3

from typing import Union, Sequence
from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import Schema

from flask import current_app as api
from chops.core.flask_extensions import db
from chops.database.models import Academic, Citation, CitationText, AcademicCitation, Keyword
from chops.utils.misc import process_word_count

blueprint = Blueprint('academics', __name__)

academic_args = {
    'page': fields.Integer(missing=1),
    'id': fields.Integer(),
    'ids': fields.DelimitedList(fields.Integer(), delimiter=','),
    'name': fields.Str(),
    'keywords': fields.DelimitedList(fields.String(), delimiter=','),
    'department': fields.Str(),
    'university': fields.Str(),
    'search': fields.Str(),
}

wordcloud_args = {
    'id': fields.Integer(),
    'min_ocurrences': fields.Integer(missing=5),
    'min_word_length': fields.Integer(missing=5),
    'limit': fields.Integer(missing=50)
}

@blueprint.route('/', methods=['GET', 'POST'])
@use_args(academic_args)
def get_academic(args):
    query = db.session.query(Academic)
    if 'id' in args:
        query = query.filter_by(id=args['id']).first()
        return jsonify(query())
    elif 'ids' in args:
        query = query.filter(Academic.id.in_(args['ids'])).all()
        return jsonify([r() for r in query])
    elif 'search' in args:
        query = query.filter(Academic.name.contains(args['search'])) \
            .paginate(args['page'], api.config['POSTS_PER_PAGE'], False) \
            .items
        return jsonify({'page': args['page'], 'results': [r() for r in query]})

    if 'name' in args:
        query = query.filter(Academic.name.contains(args['name']))
    if 'department' in args or 'university' in args:
        pass
    if 'keywords' in args:
        kws = [kw.replace('+', ' ') for kw in args['keywords']]
        query = query.join(Academic.citations).join(Citation.keywords).filter(Keyword.name.in_(kws))

    query = query.paginate(args['page'], api.config['POSTS_PER_PAGE'], False).items
    return jsonify({'page': args['page'], 'results': [r() for r in query]})
