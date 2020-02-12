#!/usr/bin/env python3
import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, LargeBinary, UniqueConstraint
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from chops.flask_extensions import db
from chops.utils.database import _unique, UniqueMixin, nice_str_date

AcademicCitation = db.Table('api_academic_citations',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('academic_id', db.Integer, db.ForeignKey('api_academic.id')),
    db.Column('citation_id', db.Integer, db.ForeignKey('api_citation.id'))
)

class Academic(db.Model, UniqueMixin):
    __tablename__ = 'api_academic'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(256))
    # email = Column(String(256))
    department_id = Column(Integer, ForeignKey("api_department.id"))
    university_id = Column(Integer, ForeignKey("api_university.id"))
    wordcloud = Column(mysql.MEDIUMTEXT)

    department = relationship("Department")
    university = relationship("University")
    citations = relationship("Citation", secondary=AcademicCitation, back_populates='academics')

    __table_args__ = (UniqueConstraint('name', 'department_id', 'university_id'),)

    def __call__(self):
        return {
            'id': self.id,
            'name': self.name,
            'department': self.department.name,
            'university': self.university.name,
            'citations': [c.id for c in self.citations]
            # 'citations': [c.json() for c in self.citations]
        }

    def __str__(self):
        return "<Academic(id={}, name={}, department={}, university={})>".format(self.id, self.name, self.department.name, self.university.name)

    def unique_hash(self, *arg, **kws):
        # print(arg, kws)
        return (kws['name'], kws['department_id'], kws['university_id'])

    def unique_filter(self, query, *arg, **kws):
        # print(arg, kws)
        return query \
            .filter(self.name == kws['name']) \
            .filter(self.department_id == kws['department_id']) \
            .filter(self.university_id == kws['university_id'])

CitationKeywords = db.Table('api_citation_keywords',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('citation_id', db.Integer, db.ForeignKey('api_citation.id')),
    db.Column('keyword_id', db.Integer, db.ForeignKey('api_keyword.id')),
)

from sqlalchemy.sql import func

class Citation(db.Model, UniqueMixin):
    __tablename__ = 'api_citation'  # if you use base it is obligatory
    id = db.Column(db.Integer, primary_key=True)  # obligatory
    title = db.Column(mysql.LONGTEXT)
    url = db.Column(db.String(256))
    date_published = db.Column(db.DateTime())
    date_entered = db.Column(db.DateTime())

    academics = db.relationship("Academic", secondary=AcademicCitation, back_populates='citations')
    keywords = db.relationship("Keyword", secondary=CitationKeywords)

    __table_args__ = (db.UniqueConstraint('title', 'url'),)

    def __call__(self):
        return {
            'id': self.id,
            'academics_id': [a.id for a in self.academics],
            'title': self.title,
            'date_published': self.date_published.strftime("%d/%m/%Y"),
            'keywords': [k.name for k in self.keywords]
        }

    def __str__(self):
        return "<Citation(id={}, title={}, academics={})>".format(self.id, self.title, [a.name for a in self.academics])

    def unique_hash(self, *arg, **kws):
        return (kws['title'], kws['url'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.title == kws['title']) \
            .filter(self.url == kws['url'])

class CitationText(db.Model, UniqueMixin):
    __tablename__ = 'api_citation_text'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    citation_id = Column(Integer, ForeignKey("api_citation.id"))
    abstract = Column(LargeBinary)
    text = Column(LargeBinary)

#    __table_args__ = (UniqueConstraint('citation_i', 'url'),)

    def unique_hash(self, *arg, **kws):
        return (kws['citation_id'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.citation_id == kws['citation_id'])

class Keyword(db.Model, UniqueMixin):
    __tablename__ = 'api_keyword'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(256))
    __table_args__ = (UniqueConstraint('name'),)

    def unique_hash(self, *arg, **kws):
        return (kws['name'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.name == kws['name'])

class Department(db.Model, UniqueMixin):
    __tablename__ = 'api_department'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(256))
    __table_args__ = (UniqueConstraint('name'),)

    def __call__(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def unique_hash(self, *arg, **kws):
        return (kws['name'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.name == kws['name'])

class University(db.Model, UniqueMixin):
    __tablename__ = 'api_university'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(256))
    __table_args__ = (UniqueConstraint('name'),)

    def __call__(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def unique_hash(self, *arg, **kws):
        return (kws['name'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.name == kws['name'])
