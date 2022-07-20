import mysql.connector as conn

mydb = conn.connect(host = "database-2.cggfuymst7is.ap-south-1.rds.amazonaws.com", user = "admin", passwd = "Namish123")
cursor = mydb.cursor()
cursor.execute("select employe_id, emp_mailid from motishree.motishree_emp")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))