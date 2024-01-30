import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
cursor=mycon.cursor()
a=input("Enter: ")
cursor.execute("select count(name) from school where name='"+a+"'")
l=[]
data=cursor.fetchall()
for trans in data:
    l.append(trans)
print(l[0][0])

