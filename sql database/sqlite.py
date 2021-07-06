#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int,username text,password text)"
cursor.execute(create_table)

user = (1, 'prams', 'abcd')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'zzz', 'abcd'),
    (3, 'xxx', 'abcd')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
new_users = []
for row in cursor.execute(select_query):
    new_users.append(row)

print(new_users[0])

# save all our changes into
connection.commit()

connection.close()