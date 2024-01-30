import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
mycursor=mycon.cursor()
a=input("Enter name : ")
mycursor.execute("select * from school where Name='"+a+"'")
data=mycursor.fetchall()
for i in data:
    print(i)
