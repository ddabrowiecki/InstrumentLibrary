import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///tempinstrumentlibrary.db',
                       convert_unicode=True)

# Scoped session code from Flask for multi-threading

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


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
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'instrument_family': self.instrument_family,
            'owner': self.owner,
            'dollar_value': self.dollar_value,
            'department_id': self.department_id
        }
Base.metadata.create_all(engine)
