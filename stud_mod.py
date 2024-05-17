from util import*
from tabulate import tabulate

def create_stud():
    data=read_json()
    sno=len(data["students"])+1
    name=input("Enter name:")
    address=input("Enter address:")
    course=input("Enter course:")
    duration=input("Enter course duration:")
    
    temp_data={
        "sno": sno,
        "name": name,
        "address": address,
        "course": course,
        "duration": duration
    }
    data["students"].append(temp_data)
    write_json(data)
    
    print(f"Student {name} registered successfully")
    
def view_stud():
    data=read_json()
    table=[]
    for stud in data["students"]:
        row=[stud["sno"],stud["name"],stud["address"],stud["course"],stud["duration"]]
        table.append(row)
    print(tabulate(table,headers=["sno","name","address","course","duration"],tablefmt="fancy_grid"))
    
    # print("sno\tname\taddress\tcourse\tduration")
    # for stud in data["students"]:
    #     print(f"{stud['sno']}\t{stud['name']}\t{stud["address"]}\t{stud["course"]}\t{stud["duration"]}")
    
def upd_stud():
    view_stud()
    sno=int(input("Enter the sno you want to update:"))
    data=read_json()
    for stud in data["students"]:
        if sno==stud["sno"]:
            print("What would you like to update?")
            print("1.NAME\t2.ADDRESS\t3.COURSE\t4.DURATION")
            choice=int(input("Enter your choice[1,2,3,4]:"))
            if choice==1:
                stud["name"]=input("Enter updated name:")
            elif choice==2:
                stud["address"]=input("Enter updated address:")
            elif choice==3:
                stud["course"]=input("Enter updated address:")
            else:
                stud["duration"]=input("Enter updated duration:")
                
            print("UPDATED SUCCESSFULLY")
    write_json(data)
                
    

def del_stud():
    view_stud()
    sno=int(input("Enter the sno you want to delete:"))
    data=read_json()
    name=""
    for stud in data["students"]:
        if sno==stud["sno"]:
            name=stud["name"]
            data["students"].remove(stud)
            
    i=1
    for stud in data["students"]:
        stud["sno"]=i
        i+=1
    write_json(data)
    if name!="":
        print(f"Student {name} is deleted successfully")   
            
            
            
    