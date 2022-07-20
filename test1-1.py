import mysql.connector as conn

mydb = conn.connect(host="database-2.cggfuymst7is.ap-south-1.rds.amazonaws.com", user = "admin", passwd = "Namish123")
cursor = mydb.cursor()

#cursor.execute("create database Employee2")
#a = "create table Employee2.emp_details(emp_id int(10), emp_name varchar(80), emp_ads varchar(80), emp_salary int(8), emp_email varchar(30))"
#cursor.execute(a)

#p = "insert into Employee2.emp_details values (12, 'Motishree', 'Bangalore', 1000, 'm@gmail.com')"
#cursor.execute(p)
#q = "insert into Employee2.emp_details values (13, 'Deepak', 'Bhubaneswar', 500, 'd@gmail.com')"
#cursor.execute(q)
#r = "insert into Employee2.emp_details values (20, 'Namish', 'Kasavanahalli', 750, 'n@gmail.com')"
#cursor.execute(r)
#mydb.commit()
#print(cursor.fetchall())

#s = "select * from Employee2.emp_details"
#cursor.execute(s)
#for i in cursor.fetchall():
#    print(i)

t = "select emp_id, emp_name, emp_salary from Employee2.emp_details"
cursor.execute(t)
l = []
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l))