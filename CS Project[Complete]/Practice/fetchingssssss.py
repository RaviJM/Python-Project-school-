import mysql.connector
myconxx=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="practice")
cursorxx=myconxx.cursor()
cursorxx.execute("select name from school")
dataxx=cursorxx.fetchall()
for i in dataxx:
    print(i)
