# 22) Write a Python program to insert data into an SQLite3 database and fetch it.

import os
import sqlite3

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

conn = sqlite3.connect("Example.db")

query = conn.cursor()

query.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ('Paras Rana', 20, 'A'))
query.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ('Pavan Rana', 22, 'B'))
query.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ('Jay Paatel', 18, 'c'))

conn.commit()
conn.close()

print("\n-> Student added succesfully.")

