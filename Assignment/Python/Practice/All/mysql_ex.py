import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2530",
        database="practice"
    )

    query = conn.cursor()

    # query.execute("SELECT * FROM employee")
    # results = query.fetchall()

    # for row in results:
    #     print(row)

    qry = "update employee set name='paras' where eid=1"
    query.execute(qry)
except Exception as e:
    print(e)
else:
    print("Success")

finally:
    conn.commit()
    conn.close()

