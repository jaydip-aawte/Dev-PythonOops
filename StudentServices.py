#in services we will perform operations on the data file
import os
from migration import Migration
from Student import Student

class StudentService:
    def create(CreateStudentRequest):
        
        print("here data list will be represented")

    def update(CreateStudentRequest):
        print("Data will be printed here")
    
    def find(CreateStudentRequest):
        print("to search student in list")
    
    def delete(id):
        std_obj=Student(str(len(StudentList)+1),name, address,age)
        StudentList.append(std_obj)
        Migration.updatefile(StudentList,filename)
