import mysql.connector as conn

mydb = conn.connect(host = "database-2.cggfuymst7is.ap-south-1.rds.amazonaws.com", user = "admin", passwd = "Namish123")
cursor = mydb.cursor()
#cursor.execute("create database motishree")

s = "create table motishree.motishree_emp(employe_id int(10)  , emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
q1 = cursor.execute(s)

