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


# exercises on : https://www.w3resource.com/sql-exercises/sql-retrieve-from-table.php


"""
ord_no      purch_amt   ord_date    customer_id  salesman_id
----------  ----------  ----------  -----------  -----------
70001       150.5       2012-10-05  3005         5002
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
"""


drop_table = """
DROP TABLE salesman
"""
execute_query(connection, query=drop_table)

drop_table = """
DROP TABLE nobel_prize
"""
execute_query(connection, drop_table)
create_table = """
CREATE TABLE salesman(
 ord_no INTEGER NOT NULL,
 purch_amt FLOAT NOT NULL,
 ord_date DATE NOT NULL,
 customer_id INTEGER NOT NULL,
 salesman_id INTEGER NOT NULL);
"""

execute_query(connection, create_table)

# populate database
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

    # # adds quote
    # i = 0
    # while i < _len-1:

    #     if string[i] == ',':
    #         if i > 0 and string[i-1] not in (f"{x}" for x in range(0,9)) and string[i-1] not in ('-', '.'):
    #             _tmp = string[i-1:]
    #             string[i-1] = "'"
    #             string[:i] = _tmp
    #             _len += 1
    #         if i < _len -1 and string[i+1] not in (f"{x}" for x in range(0,9)) and string[i+1] not in ('-', '.'):
    #             _tmp = string[i+1:]
    #             string[i+1] = "'"
    #             string[:i+1] = _tmp
    #             _len += 1
    #     i += 1

    string = "".join(string)

    return "(" + string.replace(" ", "") + ")"
add_entries = """
INSERT INTO salesman (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES 
(70001,      150.5,       2012-10-05,  3005,         5002),
"""
add_entries+= f'{parse("70009       270.65      2012-09-10  3001         5005")},'
add_entries+= f'{parse("70002       65.26       2012-10-05  3002         5001")},'
add_entries+= f'{parse("70004       110.5       2012-08-17  3009         5003")},'
add_entries+= f'{parse("70004       110.5       2012-08-17  3009         5003")},'
add_entries+= f'{parse("70007       948.5       2012-09-10  3005         5002")},'
add_entries+= f'{parse("70005       2400.6      2012-07-27  3007         5001")},'
add_entries+= f'{parse("70008       5760        2012-09-10  3002         5001")},'
add_entries+= f'{parse("70010       1983.43     2012-10-10  3004         5006")},'
add_entries+= f'{parse("70003       2480.4      2012-10-10  3009         5003")},'
add_entries+= f'{parse("70012       250.45      2012-06-27  3008         5002")},'
add_entries+= f'{parse("70011       75.29       2012-08-17  3003         5007")},'
add_entries+= f'{parse("70013       3045.6      2012-04-25  3002         5001")};'

print(add_entries)

execute_query(connection, add_entries)

# ex: From the following table, write a SQL query to identify the unique salespeople ID. Return salesman_id.  

unique_query = """
SELECT  ord_no, salesman_id FROM salesman GROUP BY salesman_id;
"""

print("exo  1", execute_query(connection, unique_query))

# nobel prize table
"""
YEAR SUBJECT                   WINNER                                        COUNTRY                CATEGORY
---- ------------------------- --------------------------------------------- ------------------------- ------------
1970 Physics                   Hannes Alfven                                 Sweden                 Scientist
1970 Physics                   Louis Neel                                    France                 Scientist
1970 Chemistry                 Luis Federico Leloir                          France                 Scientist
1970 Physiology                Ulf von Euler                                 Sweden                 Scientist
1970 Physiology                Bernard Katz                                  Germany                Scientist
1970 Literature                Aleksandr Solzhenitsyn                        Russia                 Linguist
1970 Economics                 Paul Samuelson                                USA                    Economist
1970 Physiology                Julius Axelrod                                USA                    Scientist
1971 Physics                   Dennis Gabor                                  Hungary                Scientist
1971 Chemistry                 Gerhard Herzberg                              Germany                Scientist
1971 Peace                     Willy Brandt                                  Germany                Chancellor
1971 Literature                Pablo Neruda                                  Chile                  Linguist
1971 Economics                 Simon Kuznets                                 Russia                 Economist
1978 Peace                     Anwar al-Sadat                                Egypt                  President
1978 Peace                     Menachem Begin                                Israel                 Prime Minister
1987 Chemistry                 Donald J. Cram                                USA                    Scientist
1987 Chemistry                 Jean-Marie Lehn                               France                 Scientist
1987 Physiology                Susumu Tonegawa                               Japan                  Scientist
1994 Economics                 Reinhard Selten                               Germany                Economist
1994 Peace                     Yitzhak Rabin                                 Israel                 Prime Minister
1987 Physics                   Johannes Georg Bednorz                        Germany                Scientist
1987 Literature                Joseph Brodsky                                Russia                 Linguist
1987 Economics                 Robert Solow                                  USA                    Economist
1994 Literature                Kenzaburo Oe                                  Japan                  Linguist
"""

# ex2 find the Nobel Prize winner in ‘Literature’ for 1971. Return winner. 

print(" exo 2 ")
nobel_prize_table = """
CREATE TABLE IF NOT EXISTS nobel_prize (
year DATE NOT NULL,
subject TEXT NOT NULL CHECK (subject in ('Physics', 'Chemistry', 'Literature', 'Physiology', 'Economics', 'Peace')),
winner TEXT NOT NULL,
country TEXT NOT NULL,
category TEXT NOT NULL
);
"""
#CHECK (subject in ('Physics', 'Chemistry', 'Literature', 'Physiology', 'Economics', 'Peace'))

execute_query(connection, nobel_prize_table)

add_query = """
INSERT INTO nobel_prize (year, subject, winner, country, category) VALUES
"""
data = """1970 'Physics'                   'Hannes Alfven'                                 'Sweden'                 'Scientist'
1970 'Physics'                   'Louis Neel'                                    'France'                 'Scientist'
1970 'Chemistry'                 'Luis Federico Leloir'                          'France'                 'Scientist'
1970 'Physiology'                'Ulf von Euler'                                 'Sweden'                 'Scientist'
1970 'Physiology'                'Bernard Katz'                                  'Germany'                'Scientist'
1970 'Literature'                'Aleksandr Solzhenitsyn'                        'Russia'                 'Linguist'
1970 'Economics'                 'Paul Samuelson'                                'USA'                    'Economist'
1970 'Physiology'                'Julius Axelrod'                                'USA'                    'Scientist'
1971 'Physics'                   'Dennis Gabor'                                  'Hungary'                'Scientist'
1971 'Chemistry'                 'Gerhard Herzberg'                              'Germany'                'Scientist'
1971 'Peace'                     'Willy Brandt'                                  'Germany'                'Chancellor'
1971 'Literature'                'Pablo Neruda'                                  'Chile'                  'Linguist'
1971 'Economics'                 'Simon Kuznets'                                 'Russia'                 'Economist'
1978 'Peace'                     'Anwar al-Sadat'                                'Egypt'                  'President'
1978 'Peace'                     'Menachem Begin'                                'Israel'                 'Prime Minister'
1987 'Chemistry'                 'Donald J. Cram'                                'USA'                    'Scientist'
1987 'Chemistry'                 'Jean-Marie Lehn'                               'France'                 'Scientist'
1987 'Physiology'                'Susumu Tonegawa'                               'Japan'                  'Scientist'
1994 'Economics'                 'Reinhard Selten'                               'Germany'                'Economist'
1994 'Peace'                     'Yitzhak Rabin'                                 'Israel'                 'Prime Minister'
1987 'Physics'                   'Johannes Georg Bednorz'                        'Germany'                'Scientist'
1987 'Literature'                'Joseph Brodsky'                                'Russia'                 'Linguist'
1987 'Economics'                 'Robert Solow'                                  'USA'                    'Economist'
1994 'Literature'                'Kenzaburo Oe'                                  'Japan'                  'Linguist'"""

data = data.splitlines()

for i, d in enumerate(data):

    add_query += f"{parse(d)}"
    add_query += "," if i < len(data) - 1 else ";"

print(add_query)

execute_query(connection, add_query)

winner_query = """SELECT winner FROM nobel_prize
                WHERE subject='Literature' AND year=1971
                """

print(execute_query(connection, winner_query))

# From the following table, write a SQL query to find the Nobel Prize winners in the field of ‘Physics’ since 1950. Return winner. 

winner_since_1950 = """
SELECT winner FROM nobel_prize WHERE subject='Physics' AND year>1950 GROUP BY winner;
"""

print(execute_query(connection, winner_since_1950))

# Write a SQL query to display all details of the Prime Ministerial winners after 1972 

prime_minister_winner = """SELECT winner FROM nobel_prize WHERE category='PrimeMinister' AND year > 1972;
"""

print(execute_query(connection, prime_minister_winner))
# Winners with First Name Louis

winner_named_louis ="""
SELECT winner FROM nobel_prize WHERE  winner LIKE 'Louis%';
"""
print(execute_query(connection, winner_named_louis))

#  1970 Winners Excluding Physiology & Economics

winner_1970_without_eco_physiol = """
SELECT winner, subject FROM nobel_prize WHERE year=1970 AND subject NOT IN ('Physiology', 'Economics');
"""
print(execute_query(connection, winner_1970_without_eco_physiol))

# Physiology Before 1971 & Peace After 1974

winner_physiol_peace = """
SELECT winner, subject, year FROM nobel_prize WHERE (subject='Physiology' AND year<1971) OR (subject='Peace' AND year>1974) GROUP BY winner;
"""

print(execute_query(connection, winner_physiol_peace))

# Winners Excluding Subjects Starting with P

winner_sub_not_starting_with_P = """
SELECT winner, subject FROM nobel_prize WHERE subject NOT LIKE 'P%' ORDER BY subject;
"""

print(execute_query(connection, winner_sub_not_starting_with_P))

#  Ordered 1970 Nobel Prize Winners

nobel_prize_1970 = """
SELECT winner, year FROM nobel_prize WHERE year=1970 ORDER BY winner;
"""

print(execute_query(connection, nobel_prize_1970))


### exo3 
"""
 PRO_ID PRO_NAME                       PRO_PRICE    PRO_COM
------- ------------------------- -------------- ----------
    101 Mother Board                    3200.00         15
    102 Key Board                        450.00         16
    103 ZIP drive                        250.00         14
    104 Speaker                          550.00         16
    105 Monitor                         5000.00         11
    106 DVD drive                        900.00         12
    107 CD drive                         800.00         12
    108 Printer                         2600.00         13
    109 Refill cartridge                 350.00         13
    110 Mouse                            250.00         12
"""
# instruction to create new table

create_table_query = """
CREATE TABLE IF NOT EXISTS item_mast (
pro_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 101,
pro_name TEXT NOT NULL,
pro_price FLOAT NOT NULL,
pro_com INTEGER NOT NULL 
);
"""
print("---exo3---")
execute_query(connection, create_table_query)

data = """101 'Mother Board'                    3200.00         15
102 'Key Board'                        450.00         16
103 'ZIP drive'                        250.00         14
104 'Speaker'                          550.00         16
105 'Monitor'                         5000.00         11
106 'DVD drive'                        900.00         12
107 'CD drive'                         800.00         12
108 'Printer'                         2600.00         13
109, 'Refill cartridge'                 350.00         13
110 'Mouse'                            250.00         12
"""

data = data.splitlines()

add_query = """
INSERT INTO item_mast (pro_id, pro_name, pro_price, pro_com) VALUES
"""
for i, d in enumerate(data):

    add_query += f"{parse(d)}"
    add_query += "," if i < len(data) - 1 else ";"

print(add_query)
execute_query(connection, add_query)

# exercises :
# Products in Price Range Rs.200-600

query_product_in_range = """
SELECT * FROM item_mast WHERE (pro_price BETWEEN 200 AND 600);
"""

print(execute_query(connection, query_product_in_range))

# Average Price for Manufacturer Code 16

avg_price_query = """
SELECT AVG(pro_price) FROM item_mast WHERE pro_com=16;
"""
print(execute_query(connection, avg_price_query))

# write a SQL query to display the pro_name as 'Item Name' and pro_priceas 'Price in Rs.'  

change_name_query = """
SELECT pro_name AS 'Item Name', pro_price AS 'Price in Rs' FROM item_mast;"""

print(execute_query(connection, change_name_query))

# Average Price per Company

avg_per_company_query = """
SELECT AVG(pro_price), pro_com FROM item_mast GROUP BY pro_com;
"""

print(execute_query(connection, avg_per_company_query))
# cheapest item

chepeast_item_query = """
SELECT pro_name, MIN(pro_price) FROM item_mast;
"""

print(execute_query(connection, chepeast_item_query))
# Employees in Department 57

connection.close()