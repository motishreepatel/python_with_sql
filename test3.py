import mysql.connector as conn

mydb = conn.connect(host = "database-2.cggfuymst7is.ap-south-1.rds.amazonaws.com", user = "admin", passwd = "Namish123")
cursor = mydb.cursor()
s = "insert into motishree.motishree_emp values (101,'motishree','motishree@gmail.com',100,30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()
cursor.execute("select * from motishree.motishree_emp")
for i in cursor.fetchall():
    print(i)