import control
print()
print()
print("================================Welcome to HRD Travels==================================")
print()
print("***You Say it, We Book it !***")
print()
print()

def main():
    print("1) Book Ticket"+'\n'
          "2) View your Booking"+'\n'
          "3) Cancel Ticket"+'\n'
          "4) Exit")
    print()
    choice=int(input("Please Enter your choice (1-4): "))
    print()

    if choice==1:
        control.book()
        control.choices()

    elif choice==2:
        control.view()
        control.choices()

    elif choice==3:
        control.cancel()
        control.choices()

    elif choice==4:
        print()
        print()
        print("   ============================= THANK YOU ===============================")
        quit()

    else:
        print()
        print("Oops! Please Enter a valid Choice")
        control.choices()
        
main()
