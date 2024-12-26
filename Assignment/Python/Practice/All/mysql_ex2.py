import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    database = "practice",
    username = "root",
    password = "root1"
)

query = conn.cursor()

qry = "select * from employee"
query.execute(qry)

results = query.fetchall()
for row in results:
    print(row)

print("success")
conn.commit()
conn.close()