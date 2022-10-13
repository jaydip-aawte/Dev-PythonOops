#in services we have only performed write operation
import os
from Repository import Repository

class StudentServices:
    def create(CreateStudentRequest,filename):
        name,address,age=CreateStudentRequest.name,CreateStudentRequest.address,CreateStudentRequest.age
        response=Repository.addrow(name,address,age,filename)
        return response

    def update(CreateStudentRequest):
        print("Data will be printed here")
    
    def find(CreateStudentRequest):
        print("to search student in list")
    
    def delete(id):
        # std_obj=Student(str(len(StudentList)+1),name, address,age)
        # StudentList.append(std_obj)
        # Migration.updatefile(StudentList,filename)
        print("alt")
