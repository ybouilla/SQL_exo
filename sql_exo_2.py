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

def parse(string):
    string = list(string)
    _is_start, _is_end = True, False
    _replaced = False
    _is_same_word = False
    _len = len(string)
    for i, c in enumerate(string):

        if c != " " and i<_len -1 and string[i +1] == ' ':
            if c not in (f"{x}" for x in range(0,9)):
                _is_same_word = True
                _is_end = False
            continue
        
        elif c == " " and not _replaced and not _is_same_word:
            _replaced = True
            _is_same_word = False
            _is_end = True
            _is_start = False
            string[i] = ','
        
        elif c != ' ':
            _replaced = False
        elif _is_same_word:
            _is_same_word = False
    string = "".join(string)

    return "(" + string.replace(" ", "") + ")"

connection = create_connection("E:\\sm_app2.sqlite")

drop_tables = """
DROP TABLE IF EXISTS salesman;
"""
execute_query(connection, drop_tables)
drop_tables = """
DROP TABLE IF EXISTS customer;
"""
execute_query(connection, drop_tables)

drop_tables = """
DROP TABLE IF EXISTS orders;
"""

execute_query(connection, drop_tables)
"""
 salesman_id |    name    |   city   | commission 
-------------+------------+----------+------------
        5001 | James Hoog | New York |       0.15
        5002 | Nail Knite | Paris    |       0.13
        5005 | Pit Alex   | London   |       0.11
        5006 | Mc Lyon    | Paris    |       0.14
        5007 | Paul Adam  | Rome     |       0.13
        5003 | Lauson Hen | San Jose |       0.12

 customer_id |   cust_name    |    city    | grade | salesman_id 
-------------+----------------+------------+-------+-------------
        3002 | Nick Rimando   | New York   |   100 |        5001
        3007 | Brad Davis     | New York   |   200 |        5001
        3005 | Graham Zusi    | California |   200 |        5002
        3008 | Julian Green   | London     |   300 |        5002
        3004 | Fabian Johnson | Paris      |   300 |        5006
        3009 | Geoff Cameron  | Berlin     |   100 |        5003
        3003 | Jozy Altidor   | Moscow     |   200 |        5007
        3001 | Brad Guzan     | London     |       |        5005
"""
# https://www.w3resource.com/sql-exercises/sql-joins-exercises.php

create_salesman = """
CREATE TABLE IF NOT EXISTS salesman (
salesman_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 5001,
name TEXT NOT NULL,
city TEXT NOT NULL,
commission FLOAT NOT NULL
);
"""

create_custommer = """
CREATE TABLE IF NOT EXISTS customer (
customer_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 3002,
cust_name TEXT NOT NULL,
city TEXT NOT NULL,
grade INTEGER ,
salesman_id INTEGER NOT NULL,
FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_id)
);
"""


execute_query(connection, create_salesman)

execute_query(connection, create_custommer)


# populate tables

data1 = """5001 | 'James Hoog' | 'New York' |       0.15
5002 | 'Nail Knite' | 'Paris'    |       0.13
5005 | 'Pit Alex'   | 'London'   |       0.11
5006 | 'Mc Lyon'    | 'Paris'    |       0.14
5007 | 'Paul Adam'  | 'Rome'     |       0.13
5003 | 'Lauson Hen' | 'San Jose' |       0.12
"""
data2 = """3002 | 'Nick Rimando'   | 'New York'   |   100 |        5001
        3007 | 'Brad Davis'     | 'New York'   |   200 |        5001
        3005 | 'Graham Zusi'    | 'California' |   200 |        5002
        3008 | 'Julian Green'   | 'London'     |   300 |        5002
        3004 | 'Fabian Johnson' | 'Paris'      |   300 |        5006
        3009 | 'Geoff Cameron'  | 'Berlin'     |   100 |        5003
        3003 | 'Jozy Altidor'   | 'Moscow'     |   200 |        5007
        3001 | 'Brad Guzan'     | 'London'     |     NULL  |        5005"""

data1 = data1.splitlines()

add_query = """
INSERT INTO salesman (
salesman_id, name, city, commission
) VALUES
"""
for i, d in enumerate(data1):
    add_query += f'({d.replace("|", ",")})'
    add_query += ";" if i == len(data1) - 1 else ","

print(add_query)

execute_query(connection, add_query)

add_query = """
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
"""
data2 = data2.splitlines()
for i, d in enumerate(data2):
    add_query += f'({d.replace("|", ",")})'
    add_query += ";" if i == len(data2) - 1 else ","

print(add_query)

execute_query(connection, add_query)

# write a SQL query to find the salesperson and customer who reside in the same city. Return Salesman, cust_name and city. 
query1 = """
SELECT salesman.name, customer.cust_name, customer.city AS cities FROM salesman JOIN customer ON salesman.city = cities ORDER BY cities;
"""

print(execute_query(connection, query1))


'''
ord_no      purch_amt   ord_date    customer_id  salesman_id
----------  ----------  ----------  -----------  -----------
70001       150.5       2012-10-05  3005         5002
70009       270.65      2012-09-10  3001         5005
70002       65.26       2012-10-05  3002         5001customer.cust_name
70004       110.5       2012-08-17  3009         5003
70007       948.5       2012-09-10  3005         5002
70005       2400.6      2012-07-27  3007         5001
70008       5760        2012-09-10  3002         5001
70010       1983.43     2012-10-10  3004         5006
70003       2480.4      2012-10-10  3009         5003
70012       250.45      2012-06-27  3008         5002
70011       75.29       2012-08-17  3003         5007
70013       3045.6      2012-04-25  3002         5001
'''

data3 = '''70001       150.5       2012-10-05  3005         5002
70009       270.65      2012-09-10  3001         5005
70002       65.26       2012-10-05  3002         5001
70004       110.5       2012-08-17  3009         5003
70007       948.5       2012-09-10  3005         5002
70005       2400.6      2012-07-27  3007         5001
70008       5760        2012-09-10  3002         5001
70010       1983.43     2012-10-10  3004         5006
70003       2480.4      2012-10-10  3009         5003
70012       250.45      2012-06-27  3008         5002
70011       75.29       2012-08-17  3003         5007
70013       3045.6      2012-04-25  3002         5001
'''

create_table = """
CREATE TABLE IF NOT EXISTS orders (
ord_no INTEGER  PRIMARY KEY NOT NULL, 
purch_amt FLOAT NOT NULL, 
ord_date DATE, 
customer_id INTEGER NOT NULL, 
salesman_id INTEGER NOT NULL, 
FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_id));
"""

execute_query(connection, create_table)

add_query = """
INSERT INTO orders(ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
"""
data3 = data3.splitlines()
for i, d in enumerate(data3):
    add_query += f"{parse(d)}"
    add_query += ";" if i == len(data3) - 1 else ","

print(add_query)
execute_query(connection, add_query)

# write a SQL query to find those orders where the order amount exists between 500 and 2000. Return ord_no, purch_amt, cust_name, city

query2 = """
SELECT orders.ord_no, orders.purch_amt, customer.cust_name, customer.city FROM orders JOIN customer ON orders.customer_id=customer.customer_id WHERE orders.purch_amt BETWEEN 500 AND 2000 ORDER BY orders.purch_amt;
"""

print(execute_query(connection, query2))

# find the salesperson(s) and the customer(s) he represents. Return Customer Name, city, Salesman, commission. 

query3 = """
SELECT customer.cust_name, salesman.name, salesman.city,  salesman.commission FROM  salesman
INNER JOIN customer ON customer.salesman_id = salesman.salesman_id ORDER BY salesman.name;
"""

print(execute_query(connection, query3))


# find salespeople who received commissions of more than 12 percent from the company. Return Customer Name, customer city, Salesman, commission.   


query4 = """
SELECT customer.cust_name, customer.city, salesman.name, salesman.commission FROM salesman INNER JOIN customer ON customer.salesman_id=salesman.salesman_id WHERE salesman.commission > 0.12;
"""

print(execute_query(connection, query4))


# SQL query to locate those salespeople who do not live in the same city where their customers 
# live and have received a commission of more than 12% from the company. Return Customer Name, customer city, Salesman, salesman city, commission.   

query5="""
SELECT customer.cust_name, customer.city, salesman.city, salesman.commission FROM salesman INNER JOIN customer ON salesman.salesman_id = customer.salesman_id WHERE salesman.city <> customer.city AND salesman.commission > 0.12
ORDER BY customer.cust_name;
"""

print(execute_query(connection, query5))

# From the following tables write a SQL query to find the details of an order. Return ord_no, ord_date, purch_amt, Customer Name, grade, Salesman, commission

query6="""
SELECT orders.ord_no, orders.ord_date, orders.purch_amt, customer.cust_name, customer.grade, salesman.name FROM orders
 INNER JOIN customer ON orders.customer_id = customer.customer_id
 INNER JOIN salesman ON customer.salesman_id = salesman.salesman_id;
"""

print(execute_query(connection, query6))
# . Write a SQL statement to join the tables salesman, customer and orders so that the same column of each table appears once and only the relational rows are returned.  

print("++++++++++++++++++")
query7="""
SELECT * FROM orders NATURAL JOIN customer NATURAL JOIN salesman;
"""

print(execute_query(connection, query7))
# write a SQL query to display the customer name, customer city, grade, salesman, salesman city.
#  The results should be sorted by ascending customer_id.   

query8 = """
SELECT c.cust_name, c.city, c.grade, s.name, s.city FROM customer c INNER JOIN salesman s ON c.salesman_id = s.salesman_id
 ORDER BY c.customer_id;
"""
print(execute_query(connection, query8))

# write a SQL query to find those customers with a grade less than 300. Return cust_name, customer city,
#  grade, Salesman, salesmancity.
# The result should be ordered by ascending customer_id.  

# generate a report with customer name, city, order number, order date, order amount, salesperson name,
#  and commission to determine if any of the existing customers
#  have not placed orders or if they have placed orders through their salesman or by themselves. 

query9 = """
SELECT c.cust_name, c.city, o.ord_no, o.ord_date, o.purch_amt, s.name, s.commission FROM customer c LEFT OUTER JOIN orders o ON o.customer_id = c.customer_id
 LEFT OUTER JOIN salesman s ON s.salesman_id = c.salesman_id; 
"""

print(execute_query(connection, query9))
#Write a SQL statement to generate a list in ascending order of salespersons who work either for one or more customers or have not
#  yet joined any of the customers. 

query10="""
SELECT s.name FROM salesman s LEFT OUTER JOIN customer c ON s.salesman_id = c.salesman_id 
 LEFT OUTER JOIN orders o ON s.salesman_id = o.salesman_ID ORDER BY s.salesman_id;
"""

print(execute_query(connection, query10))
connection.close()