import pandas, sqlite3, sqlalchemy
from numpy import ndarray
from sqlalchemy import *

# pandas to read csv files
legend = pandas.read_csv('data/pwt8.1_LEGEND.csv')
data = pandas.read_csv('data/pwt8.1.csv', encoding='utf-8')

# import data to identify locations of countries and their country codes
world = pandas.read_csv('data/borders.csv')
# drop unnecessary columns (other country naming conventions, subregion field)
world.drop(world.columns[[0,1,3,4,8]], axis=1, inplace=True)

# sqlalchemy to import to database ??
engine = create_engine('sqlite:///:circa')

# use pandas to write to database, sqlalchemy creates connection
legend.to_sql('legend', engine, if_exists='append')
# data.to_sql('PWT_8.1', engine, if_exists='append')
world.to_sql('world_map_data', engine, if_exists='append')

SA_Countries = ("PAN","NIC","VEN","URY","SUR","PER","PRY","GUY","GUF","FLK","ECU","COL","CHL","BRA","BOL","ARG")

sa_data = data.loc[data['countrycode'].isin(SA_Countries)]
# sa_data[['countrycode','country','year','rgdpna','pop','ck','hc','csh_x','csh_m','index']
sa_data.to_sql('pwt8_sa', engine, if_exists='append')