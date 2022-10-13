#main file to Run the Project 
from input_handeler import InputHandeler
from Student import Student
import os

if __name__=="__main__":
    print("Program has started")
    for files in os.listdir():
     if files[-3:]=="csv":print(files)
    InputHandeler.filename=input("\n \n"+" Type File name for operations :\n")
    try:
     if(os.path.exists(InputHandeler.filename)):
        with open(InputHandeler.filename, 'r+', newline='') as reader:
                read_lst = reader.readlines()
                templist=[]
                for rd in read_lst:
                 templist=(rd.split(','))
                std_obj=Student(templist[0],templist[1],templist[2],templist[3])
                InputHandeler.StudentList.append((std_obj))
                InputHandeler.startOperation()
     else: 
            print("Please enter valid file name \n")
    except FileNotFoundError as exc:print("Encounterd Error :",exc)
