# 21) Write a Python program to create a database and a table using SQLite3. 

import os
import sqlite3

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

conn = sqlite3.connect("Example.db")

query = conn.cursor()

query.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
''')

conn.commit()
conn.close() 

print(f"\n-> Database created succesfully.")
