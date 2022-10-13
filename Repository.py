from input_handeler import InputHandeler

class Repository(object):
    def __init__(self):
        with open(InputHandeler.filename, 'r+', newline='') as reader:
                read_lst = reader.readlines()
                templist=[]
                for rd in read_lst:
                 templist=(rd.split(','))

    def save(student):
    def update(student)
