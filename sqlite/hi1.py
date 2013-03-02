import sqlite3

# create database connection
connection = sqlite3.connect("contactdb.sqlite")

# create cursor
cursor = connection.cursor()

## execute SQL query
# create table 
#cursor.execute("CREATE TABLE contacts (rid INTEGER, name TEXT, dob TEXT, email TEXT, mobile TEXT)")
 
# insert
cursor.execute("INSERT INTO contacts (rid, name, dob, email, mobile) VALUES (2, 'Lim Ah Beng', '1995-02-02', 'limahbeng@hotmail.com', '12345678')")

# select
cursor.execute("SELECT * FROM contacts")

# update



# delete
results = cursor.fetchall()

for record in results:
    print(record)

# make changes permanent
connection.commit()

# destroy database connection (and cursor)
connection.close()