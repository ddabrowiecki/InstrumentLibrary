import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Instrument(Base):
    __tablename__ = 'instrument'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    instrument_family = Column(String(250))
    owner = Column(String(250))
    dollar_value = Column(String(8))
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(Department)

engine = create_engine('sqlite:///internalinstrumentlibrary.db')

Base.metadata.create_all(engine)