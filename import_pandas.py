import pandas, sqlite3, sqlalchemy
from sqlalchemy import *

# pandas to read csv files
legend = pandas.read_csv('pwt8.1_LEGEND.csv')
data = pandas.read_csv('pwt8.1.csv')

# sqlalchemy to import to database ??
engine = create_engine('sqlite:///:main')

# use pandas to write to database, sqlalchemy creates connection
legend.to_sql('legend', engine, if_exists='append')
data.to_sql('penn_complete', engine, if_exists='append')