from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from new_db import Base, Department, Instrument
app = Flask(__name__)


engine = create_engine('sqlite:///internalinstrumentlibrary.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def addDepartment():
    department = session.query(Department).first()
    instruments = session.query(Instrument).filter_by(department_id=department.id)
    output = ''
    for i in instruments:
        output += i.name
        output += '</br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
