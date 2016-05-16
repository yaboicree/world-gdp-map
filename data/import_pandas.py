import pandas, sqlite3, sqlalchemy
from sqlalchemy import *

# pandas to read csv files
legend = pandas.read_csv('pwt8.1_LEGEND.csv')
data = pandas.read_csv('pwt8.1.csv')

# import data to identify locations of countries and their country codes
world = pandas.read_csv('borders.csv')

# sqlalchemy to import to database ??
engine = create_engine('sqlite:///:main')

# use pandas to write to database, sqlalchemy creates connection
legend.to_sql('legend', engine, if_exists='append')
data.to_sql('penn_complete', engine, if_exists='append')
world.to_sql('countries', engine)