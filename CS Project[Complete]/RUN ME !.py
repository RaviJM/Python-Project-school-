import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="CSproject")
cursor=mycon.cursor()
cursor.execute("create table transport(Sr_No varchar(20),Mode_Of_Transport char(20),Price_Per_Person int(11))")
cursor.execute("insert into transport values('1)','Plane',3000)")
cursor.execute("insert into transport values('2)','Bus',1000)")
cursor.execute("insert into transport values('3)','Train',500)")
mycon.commit()

#####

cursor.execute("create table price(MainName char(20),No_of_Members int(11),Per_Person_Price int(11),Total_Cost int(11))")
mycon.commit()

#####

cursor.execute("create table pick_up(Sr_No varchar(20),City char(20))")
cursor.execute("insert into pick_up values('1)','Udaipur')")
cursor.execute("insert into pick_up values('2)','Delhi')")
cursor.execute("insert into pick_up values('3)','Mumbai')")
cursor.execute("insert into pick_up values('4)','Banglore')")
cursor.execute("insert into pick_up values('5)','Chennai')")
mycon.commit()

#####

cursor.execute("create table destination(Sr_No varchar(20),City char(20))")
cursor.execute("insert into destination values('1)','Udaipur')")
cursor.execute("insert into destination values('2)','Delhi')")
cursor.execute("insert into destination values('3)','Mumbai')")
cursor.execute("insert into destination values('4)','Banglore')")
cursor.execute("insert into destination values('5)','Chennai')")
mycon.commit()

#####

cursor.execute("create table menu(pick_ups char(20),drop_to char(20),fare int(11))")
cursor.execute("insert into menu values('Udaipur','Delhi',899)")
cursor.execute("insert into menu values('Udaipur','Mumbai',1500)")
cursor.execute("insert into menu values('Udaipur','Banglore',3500)")
cursor.execute("insert into menu values('Udaipur','Chennai',4000)")
cursor.execute("insert into menu values('Delhi','Udaipur',901)")
cursor.execute("insert into menu values('Delhi','Mumbai',3500)")
cursor.execute("insert into menu values('Delhi','Banglore',4999)")
cursor.execute("insert into menu values('Delhi','Chennai',4999)")
cursor.execute("insert into menu values('Mumbai','Udaipur',1100)")
cursor.execute("insert into menu values('Mumbai','Delhi',2500)")
cursor.execute("insert into menu values('Mumbai','Banglore',1238)")
cursor.execute("insert into menu values('Mumbai','Chennai',4000)")
cursor.execute("insert into menu values('Banglore','Udaipur',3500)")
cursor.execute("insert into menu values('Banglore','Delhi',4999)")
cursor.execute("insert into menu values('Banglore','Mumbai',1238)")
cursor.execute("insert into menu values('Banglore','Chennai',2000)")
cursor.execute("insert into menu values('Chennai','Udaipur',4000)")
cursor.execute("insert into menu values('Chennai','Delhi',4999)")
cursor.execute("insert into menu values('Chennai','Mumbai',4000)")
cursor.execute("insert into menu values('Chennai','Banglore',2500)")
mycon.commit()

#####

cursor.execute("create table booking(MainName char(20),MemberName char(20),Age int(11),PickUp char(20),Destination char(20),Transport char(20),TicketPrice int(11))")
mycon.commit()

#####

mycon.close()



