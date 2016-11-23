from __future__ import print_function
import os
import sqlite3

db_filename='mydatabase.db'
#
#   if DB exists - delete it
#
exists = os.path.exists(db_filename)
if exists:
    os.unlink(db_filename)
#
#   connect to DB (create it if it doesn't exist)
#
conn = sqlite3.connect(db_filename)
#
#   create a table
#
schema="""create table person (
  id integer primary key autoincrement not null,
  name text not null,
  dob  date,
  nationality text,
  gender text)
 """
conn.executescript(schema)
#
# create some data
#
people="""insert into person (name, dob,nationality,gender)
values ('Fred Bloggs', '1965-12-25','British','Male');
insert into person (name, dob,nationality,gender)
values ('Santa Claus', '968-01-01','Lap','Male');
insert into person (name, dob,nationality,gender)
values ('Tooth Fairy', '1931-03-31','American','Female');
"""
conn.executescript(people)
#
#   execute a query
#
cursor = conn.cursor()
cursor.execute("select id, name, dob,nationality,gender from person")
for row in cursor.fetchall():
    id, name, dob,nationality,gender = row
    print("%3d %15s %12s %10s %6s" % (id, name, dob,nationality,gender))
#
#   attempt to insert a person with no name
#
try:
    dupe="insert into person (id, dob,nationality,gender) \
    values (1,'1931-03-31','American','Female');"
    conn.executescript(dupe)
except Exception,e:
    print('Cannot insert record',e.__class__.__name__)