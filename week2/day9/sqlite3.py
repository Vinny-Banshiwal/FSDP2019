import os
import sqlite3
from pandas import DataFrame

conn=sqlite3.connect('student.db')
c=conn.cursor()
c.execute("""CREATE TABLE students(
        Student_Name TEXT,
        Student_Age INTEGER,
        Student_Roll_no INTEGER,
        Student_Branch. TEXT)""")


c.execute("INSERT INTO students VALUES('Vinny',20,1,'IT'))
c.execute("INSERT INTO students VALUES('shivi',19,2,'IT'))
c.execute("INSERT INTO students VALUES('manisha',23,3,'IT'))
c.execute("INSERT INTO students VALUES('mahima',2,4,'IT'))



