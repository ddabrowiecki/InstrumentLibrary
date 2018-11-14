from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from new_db import Base, Department, Instrument, db_session
app = Flask(__name__)

engine = create_engine('sqlite:///internalinstrumentlibrary.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/departments/<int:department_id>/instrument_list/JSON')
def departmentJSON(department_id):
    department = session.query(Department).filter_by(id=department_id).one()
    instruments = session.query(Instrument).filter_by(department_id=department_id).all()
    return jsonify(Instrument=[i.serialize for i in instruments])

@app.route('/departments/')
def departmentList():
    return render_template('main.html')

@app.route('/departments/<int:department_id>/')
def populateDepartment(department_id):
    department = session.query(Department).filter_by(id = department_id).one()
    instruments = session.query(Instrument).filter_by(department_id = department_id)
    return render_template('instrument.html', department = department, instruments = instruments)

#Function to add an instrument to the library
@app.route('/departments/<int:department_id>/new', methods = ['GET', 'POST'])
def newInstrument(department_id):
    if request.method == 'POST':
        newInstrument = Instrument(name=request.form['name'],description=request.form['description'], instrument_family=request.form['instrument_family'], owner=request.form['owner'], dollar_value=request.form['dollar_value'], department_id=department_id)
        session.add(newInstrument)
        session.commit()
        return redirect(url_for('populateDepartment', department_id=department_id))
    else:
        return render_template('new_instrument.html', department_id=department_id)

#Function to edit an instrument in the library
@app.route('/departments/<int:department_id>/<int:instrument_id>/edit', methods=['GET', 'POST'])
def editInstrument(department_id, instrument_id):
    editedInstrument = session.query(Instrument).filter_by(id=instrument_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedInstrument.name = request.form['name']
        session.add(editedInstrument)
        session.commit()
        return redirect(url_for('populateDepartment', department_id=department_id))
    else:
        return render_template('editInstrument.html', department_id=department_id, instrument_id=instrument_id, item=editedInstrument)

@app.route('/departments/<int:department_id>/<int:instrument_id>/delete', methods=['GET', 'POST'])
def deleteInstrument(department_id, instrument_id):
    itemToDelete = session.query(Instrument).filter_by(id=instrument_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('populateDepartment', department_id=department_id))
    else:
        return render_template('deleteinstrument.html', item=itemToDelete)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
