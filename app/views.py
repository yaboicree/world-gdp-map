from flask import render_template, request
from app import app
import sqlalchemy, sqlite3
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///:main')
meta = MetaData(bind=engine)

@app.route('/')
@app.route('/index')
def index():
		Penn = Table('penn_complete', meta, autoload=True)
		Legend = Table('legend', meta, autoload=True)
		Map = render_template('south_america.svg')
		return render_template('index.html', **locals())