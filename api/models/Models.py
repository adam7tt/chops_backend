#!/usr/bin/env python3
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, LargeBinary, UniqueConstraint
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from api import db
from api.utils.db_helper import _unique, UniqueMixin

AcademicCitation = Table('api_academic_citations', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('academic_id', Integer, ForeignKey('api_academic.id')),
    Column('citation_id', Integer, ForeignKey('api_citation.id'))
)

class Academic(db.Model, UniqueMixin):
    __tablename__ = 'api_academic'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(255))
    department_id = Column(Integer, ForeignKey("api_department.id"))
    university_id = Column(Integer, ForeignKey("api_university.id"))
    wordcloud = Column(mysql.MEDIUMTEXT)

    department = relationship("Department")
    university = relationship("University")
    citations = relationship("Citation", secondary=AcademicCitation, back_populates='academics')

    __table_args__ = (UniqueConstraint('name', 'department_id', 'university_id'),)

    def unique_hash(self, *arg, **kws):
        # print(arg, kws)
        return (kws['name'], kws['department_id'], kws['university_id'])

    def unique_filter(self, query, *arg, **kws):
        # print(arg, kws)
        return query \
            .filter(self.name == kws['name']) \
            .filter(self.department_id == kws['department_id']) \
            .filter(self.university_id == kws['university_id'])

CitationKeywords = Table('api_citation_keywords', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('citation_id', Integer, ForeignKey('api_citation.id')),
    Column('keyword_id', Integer, ForeignKey('api_keyword.id')),
)

class Citation(db.Model, UniqueMixin):
    __tablename__ = 'api_citation'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    title = Column(mysql.LONGTEXT)
    url = Column(String(256))
    date_published = DateTime()
    date_entered = DateTime()

    academics = relationship("Academic", secondary=AcademicCitation, back_populates='citations')
    keywords = relationship("Keyword", secondary=CitationKeywords)

    __table_args__ = (UniqueConstraint('title', 'url'),)

    def unique_hash(self, *arg, **kws):
        return (kws['title'], kws['url'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.title == kws['title']) \
            .filter(self.url == kws['url'])

class CitationText(db.Model, UniqueMixin):
    __tablename__ = 'api_citation'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    citation_id = Column(Integer, ForeignKey("api_citation.id"))
    abstract = Column(LargeBinary)
    text = Column(LargeBinary)

    __table_args__ = (UniqueConstraint('title', 'url'),)

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

    def unique_hash(self, *arg, **kws):
        return (kws['name'])

    def unique_filter(self, query, *arg, **kws):
        return query \
            .filter(self.name == kws['name'])