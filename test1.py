import mysql.connector as conn

mydb = conn.connect(host = "database-2.cggfuymst7is.ap-south-1.rds.amazonaws.com", user = "admin", passwd = "Namish123")
# need to write above line to establish connection with database
#print(mydb)
cursor = mydb.cursor() #cursor is like a pointer which will point diff. positions in table. so always we need to call this.
#cursor.execute("create database motishree")
cursor.execute("show databases")
#cursor.execute("create table motishree.motishreedetails(employee_id int(10), emp_name varchar(80), emp_mailid varchar(80), "
   #            "emp_salary int(6)), " "emp_attendance int(3)")
print(cursor.fetchall())
# always need to write these four queries when we will execute a code here