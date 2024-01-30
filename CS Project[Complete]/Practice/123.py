import mysql.connector
mycon1=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
print("Hello")
a=int(input("Jff: "))
if a==1:
    cursor1=mycon1.cursor()
    cursor1.execute("select * from school")
    data1=cursor1.fetchall()
    for z in data1:
        print(z)
elif a==2:
    cursor2=mycon1.cursor()
    cursor2.execute("select name from school")
    data2=cursor2.fetchall()
    for z in data2:
        print(z)
