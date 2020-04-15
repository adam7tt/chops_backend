#!/usr/bin/env python3

from typing import Union, Sequence
from flask import Blueprint, jsonify
from webargs import fields
from webargs.flaskparser import use_args
from marshmallow import Schema
from chops.core.flask_extensions import db
from chops.database.models import (Citation, CitationText, Academic, Keyword)
from chops.utils.misc import process_word_count

blueprint = Blueprint('citations', __name__)

citation_args = {
    'page': fields.Integer(missing=1),
    'id': fields.Integer(),
    'ids': fields.DelimitedList(fields.Integer(), delimiter=','),
    'keywords': fields.DelimitedList(fields.Integer(), delimiter=','),
    # 'academics_id': fields.DelimitedList(fields.Integer(), delimiter=','),
    'academic_id': fields.Integer(),
    'search': fields.Str()
}

wordcloud_args = {
    'id': fields.Integer(),
    'ids': fields.DelimitedList(fields.Integer(), delimiter=','),
    'min_ocurrences': fields.Integer(missing=5),
    'min_word_length': fields.Integer(missing=5),
    'limit': fields.Integer(missing=50)
}

@blueprint.route('/', methods=['GET', 'POST'])
@use_args(citation_args)
def get_citations(args):
    ret = []
    if 'id' in args:
        ret = Citation.query.filter_by(id=args['id']).first()
        return jsonify(ret())
    elif 'ids' in args:
        ret = db.session.query(Citation).filter(Citation.id.in_(args['ids'])).all()
        return jsonify([r() for r in ret])
    elif 'academic_id' in args:
        ret = db.session.query(Citation).join(Citation.academics).filter(Academic.id == args['academic_id'])
        return jsonify({'results': [r() for r in ret]})
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


@blueprint.route('/wordcloud/', methods=['GET', 'POST'])
@use_args(wordcloud_args)
def get_citation_wordcloud(args):
    ret = []
    if 'id' in args:
        ret = db.session \
                .query(CitationText) \
                .filter(CitationText.citation_id == args['id']) \
                .all()
    if 'ids' in args:
        ret = (
            db.session
              .query(CitationText)
              .filter(CitationText.citation_id.in_(args['ids']))
              .all()
        )
    if len(ret) > 0:
        return jsonify({'result': process_word_count([r() for r in ret], min_ocurrences=args['min_ocurrences'], min_word_length=args['min_word_length'], limit=args['limit'])})
    return jsonify(ret)
