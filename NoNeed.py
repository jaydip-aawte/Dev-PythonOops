class Migration:
 def updatefile(StudentList,filename):#haven't added try catch cause if file not exist it will be created
    with open(filename, 'w', newline="") as writer:
        writer.write("")
    with open(filename, 'a', newline="") as appender:
        header = "ID,NAME,ADDRESS,AGE \n"
        appender.write(header)
        for obj in StudentList:
         appender.write(obj.id+","+obj.name+","+obj.address+","+str(obj.age))
        print("File has been updated")#appending updated list in file for all operations
