import mysql.connector
mycons=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
cursor=mycons.cursor()
a=int(input("Enter age : "))
i="insert into prac(age) values({})".format(a)
cursor.execute(i)
mycons.commit()
for k in range (1,4):
    b=int(input("Enterrr merks: "))
    j="insert into prac(marks) values({})".format(b) where 
    cursor.execute(j)
    mycons.commit()
