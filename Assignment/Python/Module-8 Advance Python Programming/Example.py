
import os
import sqlite3

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

conn = sqlite3.connect("Example.db")

query = conn.cursor()

query.execute("update students set name = 'dhruv sharma' where id = 4")
query.execute("update students set name = 'KIshan Rajput' where id = 5")
query.execute("update students set name = 'Rahi Patel' where id = 6")

conn.commit()
conn.close()

print("\nsuccess.")