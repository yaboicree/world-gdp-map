# create tables in sql alchemy, not through sql schema file
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:circa', echo=True)

Base = declarative_base()


# import from pwt sheet 'Legend'
class Legend(Base): 
	__tablename__ = 'legend'

	var_name = Column(String, primary_key=True)
	var_desc = Column(String)

class Penn(Base):
	__tablename__ = 'penn'

	countrycode = Column(String, primary_key=True)
	country = Column(String)
	year = Column(Integer)
	rgdpna = Column(Float) # Real GDP PPP-2005 in USD 
	pop = Column(Integer) # population
	ck = Column(Float) # capital stock 
	hc = Column(Float) # educational attainment
	csh_x = Column(Float) # exports
	csh_m = Column(Float) # imports

# countries chosen for svg map ("PAN","NIC","VEN","URY","SUR","PER","PRY","GUY","GUF","FLK","ECU","COL","CHL","BRA","BOL","ARG")
class SA_Countries(Base):
 	__tablename__ = "SA_Countries"

 	countrycode = Column(String, primary_key=True)

# import from pwt sheet 'Data'
class Penn_Complete(Base):
	__tablename__ = 'PWT_8.1'

	countrycode = Column(String, primary_key=True)
	country = Column(String)
	currency_unit = Column(Float)
	year = Column(Integer)
	rgdpe = Column(Float)
	rgdpo = Column(Float)
	pop = Column(Float)
	emp = Column(Float)
	avh = Column(Float)
	hc = Column(Float)
	ccon = Column(Float)
	cda = Column(Float)
	cgdpe = Column(Float)
	cgdpo = Column(Float)
	ck = Column(Float)
	ctfp = Column(Float)
	cwtfp = Column(Float)
	rgdpna = Column(Float)
	rconna = Column(Float)
	rdana = Column(Float)
	rkna = Column(Float)
	rtfpna = Column(Float)
	rwtfpna = Column(Float)
	labsh = Column(Float)
	delta = Column(Float)
	xr = Column(Float)
	pl_con = Column(Float)
	pl_da = Column(Float)
	pl_gdpo = Column(Float)
	i_cig = Column(String)
	i_xm = Column(String)
	i_xr = Column(String)
	i_outlier = Column(String)
	cor_exp = Column(Float)
	statcap = Column(Float)
	csh_c = Column(Float)
	csh_i = Column(Float)
	csh_g = Column(Float)
	csh_x = Column(Float)
	csh_m = Column(Float)
	csh_r = Column(Float)
	pl_c = Column(Float)
	pl_i = Column(Float)
	pl_g = Column(Float)
	pl_x = Column(Float)
	pl_m = Column(Float)
	pl_k = Column(Float)

# geographic data from mapping dataset 
# use iso3 field to match to countrycode fields in other tables
class World(Base):
	__tablename__ = 'world_map_data'

	iso3 = Column(String, primary_key=True)
	name = Column(String)
	area = Column(Integer)
	pop2005 = Column(Integer)
	region = Column(Integer)
	lon = Column(Float)
	lat = Column(Float)

# commit all schemas to sqlite3 database 'circa' 
Base.metadata.create_all(engine)