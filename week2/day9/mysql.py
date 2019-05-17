from pandas import DataFrame
import mysql.connector

conn = mysql.connector.connect ( user='root', password='', host='localhost')
c = conn.cursor()
c.execute("DROP DATABASE student;")

c.execute("CREATE DATABASE student;")

c.execute("USE student;")

c.execute ("""CREATE TABLE student(
          name TEXT,
          AGE INTEGER,
          ROLL_NO INTEGER)""")

c.execute("INSERT INTO student VALUES ('vinny',20,3)")
