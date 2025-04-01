# see https://realpython.com/python-sql-libraries/
# learn what is CRUD (CREATE, READ, UPDATE, DELETE)

# assuming sql lite is used


import sqlite3

from sqlite3 import Error


def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Exception as e:

        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        res = cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return res.fetchall()
    except Exception as e:
        print(f"The error '{e}' occurred")


connection = create_connection("E:\\sm_app.sqlite")


drop_table ="""
DROP TABLE IF EXISTS  users2 
"""

execute_query(connection, drop_table)
create_users_table = """
CREATE TABLE  IF NOT EXISTS  users2 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT CHECK (gender IN ('M', 'F', 'N')),
  nationality TEXT,
  event_type TEXT CHECK(event_type IN ('opening', 'appointment')) NOT NULL,
  date DATETIME NOT NULL ---yyyy-MM-dd hh:mm:ss
);
"""


execute_query(connection, create_users_table) 


# update database

add_data = """
INSERT INTO users2 (name, age, gender, nationality, event_type, date) VALUES ('prout', 12, 'M', 'Swiss', 'opening', '1994-01-01 00:00:00'),
('fifi', 23, 'F', 'uk', 'appointment', '2002-12-12 00:00:00');
"""
# INSERT INTO users (name, age, gender, nationality) VALUES ('fifi', 23, 'F', 'uk');
execute_query(connection, add_data)

query_return_table = """
SELECT * FROM users2 WHERE date<'1995-01-01';
"""

print(execute_query(connection, query_return_table))

connection.close()