#!/usr/bin/env python3
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, UniqueConstraint
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship

from api import db
from api.utils.db_helper import _unique, UniqueMixin

class Academic(db.Model, UniqueMixin):
    __tablename__ = 'api_academic'  # if you use base it is obligatory
    id = Column(Integer, primary_key=True)  # obligatory
    name = Column(String(255))
    department_id = Column(Integer, ForeignKey("api_department.id"))
    university_id = Column(Integer, ForeignKey("api_university.id"))
    wordcloud = Column(mysql.MEDIUMTEXT)

    department = relationship("Department")
    university = relationship("University")

    __table_args__ = (UniqueConstraint('name', 'department_id', 'university_id'),)

    @classmethod
    def unique_hash(self, *arg, **kws):
        # print(arg, kws)
        return (kws['name'], kws['department_id'], kws['university_id'])

    @classmethod
    def unique_filter(self, query, *arg, **kws):
        # print(arg, kws)
        return query \
            .filter(self.name == kws['name']) \
            .filter(self.department_id == kws['department_id']) \
            .filter(self.university_id == kws['university_id'])

