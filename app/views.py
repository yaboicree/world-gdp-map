from flask import render_template, request
from app import app
import sqlalchemy, sqlite3
from sqlalchemy import create_engine, MetaData, Table, select, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, literal_column
from db_create import * 
from functions import * 

engine = create_engine('sqlite:///:circa')
meta = MetaData(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
@app.route('/index')
def index():
		Legend = Table('legend', meta, autoload=True)
		World = Table('world_map_data', meta, autoload=True)
		SA_Penn = Table('pwt8_sa', meta, autoload=True)
		cc = session.query(Penn_South_America.countrycode)
		return render_template('index.html', **locals())