import pandas, sqlite3
from sqlalchemy import create_engine

# pandas to read csv files
legend = pandas.read_csv('pwt8.1_LEGEND.csv')
data = pandas.read_csv('pwt8.1.csv')

# sqlalchemy to import to database ??
engine = create_engine('sqlite:///:memory')

# use pandas to write to database, sqlalchemy creates connection
#with engine.connect('sqlite:///circa.sqlite') as con:
legend.to_sql('legend', engine, if_exists='append')
data.to_sql('penn_complete', engine, if_exists='append')

#	pseudo-code for importing data to penn table
# for column in legend:
#	 if data[0] == penn[0]
#    import data