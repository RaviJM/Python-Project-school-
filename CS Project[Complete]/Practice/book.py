def book:
    import mysql.connector
    mycon1=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="project")
    cursor1=mycon1.cursor()
    s1="insert into book values({},{},{},{})
