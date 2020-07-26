import sqlite3

connection  = sqlite3.connect('data.db')

cursor = connection.cursor()

#create a table
create_table = "CREATE TABLE table2 (value1 int,value2 int)"
cursor.execute(create_table)

insert_query = "INSERT INTO table2 VALUES (?,?)"

table2Data =[
    (100,90),(75,65),(50,40),(75,65),(50,40),(75,65),(100,90)
]

cursor.executemany(insert_query,table2Data)

create_table = "CREATE TABLE table1 (value1 int)"
cursor.execute(create_table)

insert_query = "INSERT INTO table1 VALUES (?)"

table1Data = [
    (161,), (12,),(5,)
]

cursor.executemany(insert_query,table1Data)

create_table = "CREATE TABLE table3 (value1 real)"
cursor.execute(create_table)

insert_query = "INSERT INTO table3 VALUES (?)"

table1Data = [
    (4.1,), (4.6,),(4.67,),(4.7,),(4.3,),(4.4,)
]

cursor.executemany(insert_query,table1Data)

select_query = "SELECT * FROM table1"

for row in cursor.execute(select_query):
    print(row)

select_query = "SELECT * FROM table2"

for row in cursor.execute(select_query):
    print(row)

select_query = "SELECT * FROM table3"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()