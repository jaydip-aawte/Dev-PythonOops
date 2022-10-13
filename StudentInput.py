
class StudentInput:
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age
    
    def GetData():
     name, address, age = str(input("Please Enter Your Name: \n")), str(input("Please Enter Your address: \n")), int(input("Please Enter Your age: \n"))
     obj_input=StudentInput(name,address,age)
     return(obj_input)


