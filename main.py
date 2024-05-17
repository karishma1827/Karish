from stud_mod import*

print("Welcome to the application!")

while True:
    print("What option would you like to chose?")   
    print("1.Create record\n2.View record\n3.Update record\n4.Delete record")
    choice=input("Enter your choice[1,2,3,4]:")
    if choice in ["1","2","3","4"]:
        if choice=="1":
            print("You have chosen create record") 
            create_stud()
        elif choice=="2":
            print("You have chosen view record")
            view_stud()
        elif choice=="3":
            print("You have chosen update record")
            upd_stud()
        else:
            print("You have chosen delete record")
            del_stud()
    else:
        print("Invalid")
    cont=input("Do you want to continue?[y/n]:") 
    if cont=="y":
        continue
    else:
        print("Thank you for using the application")
        break
    
    
    
                                        
