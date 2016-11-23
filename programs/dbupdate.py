from __future__ import print_function
import sqlite3
import sys
#
#   arguments from command line
#   use: python dbupdate.py   1  Chinese
#
db_filename = 'mydatabase.db'
inid = sys.argv[1]
innat = sys.argv[2]
#
#   execute update using command line arguments
#
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
query = "update person set nationality = :nat where id = :id"
cursor.execute(query, {'id':inid, 'nat':innat})
#
#   list the persons to see changes
#   
cursor.execute("select id, name, dob,nationality,gender from person")
for row in cursor.fetchall():
    id, name, dob,nationality,gender = row
    print("%3d %15s %12s %10s %6s" % (id, name, dob,nationality,gender))

