def date_month():
    date_month=int(input("Enter Month of your travel journey(1-12) :"))
    date_month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    for date_month_check in date_month_list :
        if date_month == date_month_check :
            dm=date_month
            break
        
        elif date_month != date_month_check:
            dm="Nil"
            continue
    if dm=="Nil":
      control.date_month()  
            
date_day=int(input("Enter Date of your travel journey(1-31) :"))
date_year=int(input("Enter Year of your travel journey(20_ _) :"))


print(date_day,"/",date_month,"/20",date_year)
