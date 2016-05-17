from flask import Flask
from flask import render_template
from sqlalchemy import create_engine, Table, Column
from sqlalchemy.orm import sessionmaker

SA_Countries = ("PAN","NIC","VEN","URY","SUR","PER","PRY","GUY","GUF","FLK","ECU","COL","CHL","BRA","BOL","ARG")
engine = create_engine('sqlite:///:main:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def get_SA_vals(var):
	country_vals = {}
	for nacion, val in session.query(Table('penn_complete').countrycode,Table('penn_complete').var):
		if nacion in SA_Countries:
			country_vals[nacion] = val
		return country_vals
	# for nacion in SA_Countries:
	# 	session.query(penn_complete.var).filter(penn_complete.countrycode)


# find max of a var for countries 
def find_max(var):
	max = 0
	for val in get_SA_vals(var).values():
		if val > max:
			max = val
	return max


# set color based on the max for the var
def gradient(var):
	find_max(var) / [nacion].get_var


if __name__=='__main__':
   print find_max('pop')

# app = Flask(__name__)
# app.config['DEBUG'] = True