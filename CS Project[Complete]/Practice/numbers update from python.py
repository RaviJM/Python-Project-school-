import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
cursor=mycon.cursor()
a=1
n=input("E ")
cursor.execute("update school set rollno={} where name='{}'".format(a,n))
mycon.commit()
