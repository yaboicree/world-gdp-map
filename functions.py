from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from db_create import Penn_South_America 


engine = create_engine('sqlite:///:circa', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

#### utility functions ####

# get all vals for a given value in a given year
# def get_vals(var, year):
# 	country_vals = {}
# 	from db_create import Penn_South_America
# 	for cdata in session.query(Penn_South_America).filter('year' == year):
# 		nacion = cdata['countrycode']
# 		val = cdata[var]
# 		country_vals[nacion] = val
# 	return country_vals

def get_vals(var, year):
	country_vals = {}
	for nacion, val in session.query(Penn_South_America.countrycode, getattr(Penn_South_America,var)).filter_by(year = year):
		country_vals[nacion] = val
	return country_vals


# find max of a var for countries 
def find_max(var, year):
	maxval = 0
	for val in get_vals(var, year).values():
		if val > maxval:
			maxval = val
	return maxval


# for table: can be Penn_South_America, Legend, World???
def data(cc):
	dt = []
	# store data in form of dict, key = country code + year, value = dict of vals
	for u in session.query(Penn_South_America).filter_by(countrycode = cc):
		dt.append(u.__dict__)
	return dt

# input results from data to get the data from one year for one country
def data_year(cc, year):
	for nacion_year in data(cc):
		if nacion_year['year'] == year:
			return nacion_year


# set color based on their max for the var
def gradient(cc, var, year):
	# base color = aqua
	color = [153,51,255]

	max = find_max(var, year)
	data_for_year_and_country = data_year(cc, year)
	this_var = data_for_year_and_country[var]

	#darkest color
	if (this_var / max) > .9:
		return color

	if (this_var / max) > .6:
		red = int(color[0] + 0.2 * color[0])
		green = int(color[1] + 0.2 * color[1])
		blue = int(color[2] + 0.2 * color[2])
		return [red,green,blue]

	if (this_var / max) > .3:
		red = int(color[0] + 0.4 * color[0])
		green = int(color[1] + 0.4 * color[1])
		blue = int(color[2] + 0.4 * color[2])
		return [red,green,blue]

	red = int(color[0] + 0.6 * color[0])
	green = int(color[1] + 0.6 * color[1])
	blue = int(color[2] + 0.6 * color[2])
	return [red,green,blue]


# find a generator that will generate nice-looking colors, change every time variable changes?
# def set_color():
# 	import random
# 	red = random.randint(0, 255)
# 	blue = random.randint(0, 255)
# 	green = random.randint(0, 255)
# 	color = [red,green,blue]
# 	return color

