
import os
import sqlite3

os.chdir("D:\\paras\\Assignment\\Python\\Practice\\All")

conn = sqlite3.connect("sqlite3_ex.db")

query = conn.cursor()

# query.execute("create table student (id integer primary key AUTOINCREMENT, name varchar(20), city varchar (20))")

# query.execute("drop table student")

query.execute("INSERT INTO student (name, city) VALUES (?, ?)", ('Paras Rana', 'Surat'))
query.execute("INSERT INTO student (name, city) VALUES (?, ?)", ('Pavan Rana', 'BAroda'))
query.execute("INSERT INTO student (name, city) VALUES (?, ?)", ('Jay Paatel', 'Ahmedabad'))



conn.commit()
conn.close()

print("Success.")