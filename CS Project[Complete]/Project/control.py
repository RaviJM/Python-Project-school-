#########################################################################
def book():
    import mysql.connector
    mycon1=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="CSproject")

    print("Please fill up the details given below to BOOK your Ticket-")
    print()
    main_name=input("Head Name: ")
    main_name_lowered = main_name.lower()
    
    cursor_search_name=mycon1.cursor()
    cursor_search_name.execute("select lower(MainName) from price")
    data_search_name=cursor_search_name.fetchall()
    search_list=[]
    for search_names in data_search_name :
        search_list.append(search_names)
    for ij in range (0,(len(search_list))):
        if search_list[ij][0]==main_name_lowered :
            print()
            print("  Oops! Name already Taken ! ")
            print(" Try some other Name ")
            return
    
    mobile=int(input("Mobile no.: "))
    oomobile=str(mobile)
    if len(oomobile) <10:
        print("  Oops! Please Enter 10 digit mobile number")
        print()
        return
    elif len(oomobile) >10:
        print("  Oops! Please Enter 10 digit mobile number")
        print()
        return     
        
    print()



    print("Select YOUR CITY from below: ")                              # for viewing my_city table #
    print()
    print("|Sr.no | City |")
    print()
    cursor2=mycon1.cursor()
    cursor2.execute("select * from pick_up")
    data2=cursor2.fetchall()
    for my_city_name in data2:
        print(my_city_name)
    print()
    mycity_number=int(input("Enter choice(1-5): "))
    if mycity_number==1:
        mycity="Udaipur"
    elif mycity_number==2:
        mycity="Delhi"
    elif mycity_number==3:
        mycity="Mumbai"
    elif mycity_number==4:
        mycity="Banglore"
    elif mycity_number==5:
        mycity="Chennai"
    elif mycity_number >5:
        print()
        print("  Sorry..No other options Available")
        print("  Return to View Choices or Quit")
        print()
        return
    print()
    print("Your Pick_Up city is ",mycity)
    print()
    print("Available Destinations from Your City are--")
    print()
    print("| FROM   |  TO    | FARE PRICE |")
    print()

    cursor_menu=mycon1.cursor()
    cursor_menu.execute("select * from menu where pick_ups='"+mycity+"'")
    data_menu=cursor_menu.fetchall()
    for menus in data_menu:
        print(menus)
    print()
    print()

    print("Select your DESTINATION from below : ")                       # for viewing destination table #
    print()
    print("|Sr.no | Destination|")
    print()
    cursor1=mycon1.cursor()
    cursor1.execute("select * from destination")
    data1=cursor1.fetchall()
    for dest in data1:
        print(dest)
    print()
    destination_number=int(input("Enter choice(1-5): "))
    if destination_number==mycity_number:
        print()
        print("   Oops! Cannot keep SAME Destination and Pickup !")
        print("   Return to View Choices or Quit")
        return
    elif destination_number==1:
        destination="Udaipur"
    elif destination_number==2:
        destination="Delhi"
    elif destination_number==3:
        destination="Mumbai"
    elif destination_number==4:
        destination="Banglore"
    elif destination_number==5:
        destination="Chennai"
    elif destination_number >5:
        print()
        print("  Sorry..No other options Available")
        print("  Return to View Choices or Quit")
        print()
        return
    print()
    print("Your Destination is ",destination)
    print()
    
    print("Select Mode of Transport from below: ")                    # for viewing transport table #
    print()
    print()
    print("|Sr.no| Transport| Price|")
    print()
    cursor3=mycon1.cursor()
    cursor3.execute("select * from transport")
    data3=cursor3.fetchall()
    for trans in data3:
        print(trans)
    print()
    mode_number=int(input("Enter choice(1-3): "))
    if mode_number==1:
        mode="Plane"
        pprice=3000
    elif mode_number==2:
        mode="Bus"
        pprice=1000
    elif mode_number==3:
        mode="Train"
        pprice=500
    elif mode_number >3:
        print()
        print("  Sorry..No other options Available")
        print("  Return to View Choices or Quit")
        print()
        return
    print()
    print("Your Travelling mode is ",mode," with Per Person TRANSPORTATION Price of Rs",pprice)
    print()

    a=int(input("Enter number of members travelling: "))
    print()

    ## Payment Process ##
  
    print("Proceeding for Total Cost...")
    
    tcost=0
    if mycity_number==1 and destination_number==2:
        tcost=899
    elif mycity_number==1 and destination_number==3:
        tcost=1500
    elif mycity_number==1 and destination_number==4:
        tcost=3500
    elif mycity_number==1 and destination_number==5:
        tcost=4000
    elif mycity_number==2 and destination_number==1:
        tcost=901
    elif mycity_number==2 and destination_number==3:
        tcost=3500
    elif mycity_number==2 and destination_number==4:
        tcost=4999
    elif mycity_number==2 and destination_number==5:
        tcost=4999
    elif mycity_number==3 and destination_number==1:
        tcost=1100
    elif mycity_number==3 and destination_number==2:
        tcost=2500
    elif mycity_number==3 and destination_number==4:
        tcost=1238
    elif mycity_number==3 and destination_number==5:
        tcost=4000
    elif mycity_number==4 and destination_number==1:
        tcost=3500
    elif mycity_number==4 and destination_number==2:
        tcost=4999
    elif mycity_number==4 and destination_number==3:
        tcost=1238
    elif mycity_number==4 and destination_number==5:
        tcost=2000
    elif mycity_number==5 and destination_number==1:
        tcost=4000
    elif mycity_number==5 and destination_number==2:
        tcost=4999
    elif mycity_number==5 and destination_number==3:
        tcost=4000
    elif mycity_number==5 and destination_number==4:
        tcost=2500
    per_person_total_price = (tcost+pprice)        
    final_price= per_person_total_price*a
    cursor_costing=mycon1.cursor()
    
    print()
    print()
    print("Your per person Fare Price is:",tcost)
    print("Your per person Transportation Price is:",pprice)
    print("& Number of people Travelling are:",a)
    print()
    print("So Your Final Cost is: Rs(",tcost,"+",pprice,") *",a,"= Rs",final_price)
    print()
    print()
    confirmation=input("   CONFIRM ? (press 'y' for Proceeding and Any Other Key for Cancelling): ")
    
    if confirmation=="y":
        values_costing="insert into price(MainName,No_of_Members,Per_Person_Price,Total_cost) values('{}',{},{},{})".format(main_name,a,per_person_total_price,final_price)
        cursor_costing.execute(values_costing)
        mycon1.commit()
        print()
    else:
        print()
        print("      BOOKING CANCELLED  ")
        print()
        print("========================================================================================")
        return
   
    print("Enter Names and Age of all ",a," members" )
    
    cursor4=mycon1.cursor()
    print()
    for i in range (1,a+1):
        print(i,")",end=" ")
        m_name=input("Person name: ")
        print(i,")",end=" ")
        m_age=int(input("Age: "))
        values4="insert into booking(MainName,MemberName,Age,PickUp,Destination,Transport,TicketPrice) values('{}','{}',{},'{}','{}','{}',{})".format(main_name,m_name,m_age,mycity,destination,mode,per_person_total_price)
        cursor4.execute(values4)
        mycon1.commit()
        print()
    print()
    print("                           BOOKING SUCCESSFUL !")
    print()
    print("[ Further Details regarding Payment Method will be shared to you on Mobile Number",mobile," ]")
    print()
    print("                           Thank You for Booking !!")
    print()
    print("========================================================================================")

    mycon1.close()

#########################################################################

def view():
    import mysql.connector
    mycon2=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="CSproject")
    cursor5=mycon2.cursor()
    cursor6=mycon2.cursor()
    cursor_bill=mycon2.cursor()
    print()
    print("For Viewing Your Booked Ticket-")
    print()
    ask_name=input("Enter Name of the person by whose name the Ticket has been Booked: ")
    cursor5.execute("select * from booking where mainname='"+ask_name+"'")
    data5=cursor5.fetchall()
    cursor6.execute("select count(mainname) from booking where mainname='"+ask_name+"'")
    data6=cursor6.fetchall()
    counting_list1=[]
    for counting1 in data6:
        counting_list1.append(counting1)
    exact_count1=counting_list1[0][0]
    print()
    print()
    print("================================YOUR BOOKING==========================================")
    print()
    if exact_count1 ==0:
        print(" Oops! No Ticket has been booked by such name ")
        print()
        print("========================================================================================")
        return
    elif exact_count1 !=0:
        print()
        print(" Member List--")
        print()
        print("|MainName|MemberName|Age|Pickup|Destination|Transport|PerPersonPrice|")
        print()
        for traveller_info in data5:
            print(traveller_info)
        print("                 ==========================================               ")
        print()
        print()
        print(" Your Bill-- ")
        print()
        cursor_bill.execute("select * from price where MainName='"+ask_name+"'")
        data_bill=cursor_bill.fetchall()
        print("|MainName|No.of Members|PerPersonPrice|TotalCost|")
        print()
        for bill_view in data_bill:
            print(bill_view)

    print()
    print("========================================================================================")
    print()


    mycon2.close()
    
#########################################################################

def cancel():
    print("================================Cancelation Process========================================")
    print()
    import mysql.connector
    mycon3=mysql.connector.connect(host="localhost",user="root",passwd="ravi",database="CSproject")
    cursor7=mycon3.cursor()
    cursor8=mycon3.cursor()
    cursor9=mycon3.cursor()
    cursor_bill_cost=mycon3.cursor()
    cursor_bill_update1=mycon3.cursor()
    cursor_bill_update2=mycon3.cursor()
    cursor_delete=mycon3.cursor()
    
    the_name=input("Enter Name of the person by whose name the Ticket Was Booked: ")

    cursor8.execute("select count(mainname) from booking where mainname='"+the_name+"'")
    data8=cursor8.fetchall()
    counting_list2=[]
    for counting2 in data8:
        counting_list2.append(counting2)
    exact_count2=counting_list2[0][0]
    
    if exact_count2 ==0:
        print()
        print("             Oops! No Ticket has been booked by such name !")
        print()
        return
    elif exact_count2 !=0:
        print()
        sub_name=input("Enter the name of the Member whose ticket is to be Cancelled: ")
        
        cursor9.execute("select count(membername) from booking where membername='"+sub_name+"'")
        data9=cursor9.fetchall()
        counting_list3=[]
        for counting3 in data9:
            counting_list3.append(counting3)
        exact_count3=counting_list3[0][0]
        
        if exact_count3 ==0:
            print()
            print("             Oops! No Ticket has been booked by such name !")
            print()
            return
        elif exact_count3 !=0:
            listss=[]
            cursor7.execute("delete from booking where mainname='"+the_name+"' and membername='"+sub_name+"'")
            mycon3.commit()
            
            cursor_bill_cost.execute("select No_of_Members,Per_Person_Price,Total_Cost from price where MainName='"+the_name+"'")
            data_cost_bill=cursor_bill_cost.fetchall()
            for bill_details in data_cost_bill:
                listss.append(bill_details)
            aa=listss[0][0]
            bb=listss[0][1]
            cc=listss[0][2]

            aaa=aa-1
            bbb=bb
            ccc=(cc-bb)

            if aaa==0:
                cursor_delete.execute("delete from price where Mainname='"+the_name+"'")
                mycon3.commit()
            else:
                cursor_bill_update1.execute("update price set No_of_Members={} where MainName='{}'".format(aaa,the_name))
                mycon3.commit()
                cursor_bill_update2.execute("update price set Total_Cost={} where MainName='{}'".format(ccc,the_name))
                mycon3.commit()
            print()
            print()
            print("                      Ticket Cancelled Successfully!")
            print()
            print("          Your Money will be Refunded within 24 hrs.")
            print()
            print("========================================================================================")
        print()


    mycon3.close()

#########################################################################

def choices():
    import main_body_use
    print()
    choice_view=input("Press 'y' to VIEW CHOICES and 'n' to EXIT: ")
    if choice_view=="y":
        print()
        print()
        main_body_use.main()
        
    elif choice_view=="n":
        print()
        print()
        print("   ============================= THANK YOU ===============================")
        quit()
    else:
        import choicee_use
        print()
        print("Please Enter either 'y' Or 'n'")
        print()
        choicee_use.choices()

#########################################################################
