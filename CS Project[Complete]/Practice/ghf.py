import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
cursor=mycon.cursor()
cursor.execute("select * from school")
data=cursor.fetchall()
for i in data:
    print(i)
