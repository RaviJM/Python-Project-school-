def choices():
    import main_body_use
    print()
    choice_view=input("Enter 'y' to VIEW CHOICES and 'n' to EXIT: ")
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
        import control
        print()
        print("Please Enter either 'y' Or 'n'")
        print()
        control.choices()
