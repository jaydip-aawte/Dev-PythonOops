

class Repository(object):
    count=0
    def __init__(self,filename):
        with open(filename, 'r+', newline='') as reader:
                read_lst = reader.readlines()
                Repository.count=len(read_lst)
                print(len(read_lst))
                # templist=[]
                # for rd in read_lst:
                #  templist=(rd.split(','))

    def addrow(name,address,age,filename):
        rp_obj=Repository(filename)
        with open(filename, 'a', newline="") as appender:
            q=","
            header = str(Repository.count)+q+name+q+address+q+str(age)+q+"\n"
            appender.write(header)
            return("Data added with id",Repository.count)
            print("File has been updated")#appending updated list in file for all operations


    # def commit():

    # def save(student):

    # def update(student)
