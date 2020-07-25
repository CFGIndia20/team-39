import sqlite3

connection  = sqlite3.connect('data.db')

cursor = connection.cursor()

#create a table
create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text, email text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (NULL,?,?,?)"
user = ('jose','asdf','a@b.com') # a tuple

cursor.execute(insert_query,user)

#list of tuples
users = [
    ('rolf','asdg','a@bc.com'),
    ('Mike','aasdsdg','ab@b.com')
]   

cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()