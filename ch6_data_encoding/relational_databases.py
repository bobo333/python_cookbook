import sqlite3

# standard way to represent rows in python is a sequence of tuples
# when done this way it's easy to interact with the db using Python's standard
# database API
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2)
]

# connect to db
db = sqlite3.connect('database.db')

# create cursor
c = db.cursor()

# execute queries
print(c.execute('create table portfolio (symbol text, shares integer, price real)'))
db.commit()

# insert a sequence of rows
print(c.executemany('insert into portfolio values (?,?,?)', stocks))
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)

# clean up for re-use
c.execute('drop table portfolio')
db.commit()
