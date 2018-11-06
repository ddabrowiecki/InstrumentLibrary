from flask import Flask
app = Flask(__name__)
#from passlib.apps import custom_app_context as pwd_context

from sqlalchemy import create_engine, Foreign Key
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Department, Instrument

engine = create_engine('sqlite:///instrumentlibrary.db') #This connects us to the database created in database_setup.py
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')

def addRestaurant():
    department = session.query(Department).first()
    instrument = session.query(Instrument).filter_by(department_id = department.id)
    output = ''
    for i in instrument:
        output += i.name
        output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000) #1234?