#main file to Run the Project 
from Student import Student
from StudentServices import StudentServices
from StudentInput import StudentInput
import os
from operation import OperationManager#File operation class with name operation
class InputHandeler:
 sprt=","
 StudentList=[]
 filename=""
 def startOperation():
    operation_mode =(input("\n What operation you want to perform? \n  select 1 for read \n select 2 for write \n select 3  for Update entry \n select 4 to delete file permanently \n select 5 to delete row \n select 6 to exit \n"))     
    if operation_mode=="1":
        for obj in InputHandeler.StudentList[1:]:
            print("Id:"+obj.id," Name:"+obj.name," Address:"+obj.address," Age:",obj.age)

        
    elif operation_mode =="2":
            std_obj=StudentInput.GetData()
            print(StudentServices.create(std_obj,InputHandeler.filename))
           # OperationManager.addrow(InputHandeler.filename,InputHandeler.StudentList[1:], name, address, age,InputHandeler.sprt)

    elif operation_mode =="3":
        InputHandeler.refresh()
        id = str(input("Enter Id of User to update data: \n"))
        if int(OperationManager.idexist(InputHandeler.StudentList[1:],id,InputHandeler.sprt)) == 0:
            print("Sorry, id does not exist")
        else:
            name, address, age = InputHandeler.getdata()#taking new entry from user for updation
            OperationManager.updaterow(InputHandeler.filename,InputHandeler.StudentList,id,name,address,age,InputHandeler.sprt)

    elif operation_mode =="4":
        file_name = str(input("Please enter name of file: \n"))
        if os.path.exists(file_name) and os.path.isfile(file_name):
            os.remove(file_name)
            print("File Has Been Deleted Permanently")
        else:
            print("Sorry File not found")

    elif operation_mode =="5":
        InputHandeler.refresh()
        id = input("\n enter id need to be deleted \n")
        if int(OperationManager.idexist(InputHandeler.StudentList, id,InputHandeler.sprt)) == 0:print("Sorry, id does not exist")
        else:OperationManager.deleterow(InputHandeler.filename,InputHandeler.StudentList,id,InputHandeler.sprt)

    elif operation_mode =="6":
        print("Bye !!!!")

    else:
        print("Please Enter Valid Input")
    if(operation_mode!="6"):InputHandeler.startOperation()  

 def refresh():
     with open(InputHandeler.filename, 'r+', newline='') as reader:
             read_lst = reader.readlines()
             templist=[]
             StudentList=[]
             for rd in read_lst:
              templist=(rd.split(','))
              std_obj=Student(templist[0],templist[1],templist[2],templist[3])
              InputHandeler.StudentList.append((std_obj))


if __name__=="__main__":
    print("Program has started")
    for files in os.listdir():
     if files[-3:]=="csv":print(files)
    InputHandeler.filename=input("\n \n"+" Type File name for operations :\n")
    try:
     if(os.path.exists(InputHandeler.filename)):
        # with open(InputHandeler.filename, 'r+', newline='') as reader:
        #         read_lst = reader.readlines()
        #         templist=[]
        #         for rd in read_lst:
        #          templist=(rd.split(','))
        #         std_obj=Student(templist[0],templist[1],templist[2],templist[3])
        #         InputHandeler.StudentList.append((std_obj))
        #         InputHandeler.startOperation()
         print("alt")
         InputHandeler.startOperation()
     else: 
            print("Please enter valid file name \n")
    except FileNotFoundError as exc:print("Encounterd Error :",exc)
