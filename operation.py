import os

from Student import Student
class OperationManager:
 def addrow(filename,StudentList, name, address, age,sprt):
    std_obj=Student(str(len(StudentList)+1),name, address,age)
    StudentList.append(std_obj)
   # Migration.updatefile(StudentList,filename)

 def updaterow(filename,StudentList,id,name,address,age,sprt):
        updated_list=[]
        q = sprt
        ulst = id+q+name+q+address+q+str(age)+"\n"#formatting for csv format
        for obj in StudentList:
            if obj.id == id:
                obj.name=name
                obj.address=address
                obj.age=age
       # Migration.updatefile(StudentList,filename)#rewriting updated list in the csv file

 def deleterow(filename,StudentList, id,sprt):
    updated_list = []
    for obj in StudentList:
      if obj.id== id:
        StudentList.remove(obj)
    #Migration.updatefile(StudentList,filename)
    


 def idexist(StudentList, id,sprt):  #checking id before deletion
        count = 0
        for obj in StudentList:
            if (obj.id== str(id)):
                count += 1
        return count






# #############Object############
# file_handeler=HandelFile(takefilename(),",")#making object for file handeler
# ##############################


