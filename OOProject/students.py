class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def set_gender(self,new_gender):
        if new_gender=='M' or new_gender=='F' :
            self.__gender=new_gender;
        else:
            print('重打')
    def get_gender(self):
        return self.__gender


class student(Member):
    def __init__(self,new_gender,new_major,new_id):
        super().__init__(new_gender, new_major, new_id)


    def join_class(self):
        pass

    def quit_class(self):
        pass

    def borrow_resources(self):
        print('student borrow')


class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)
    def borrow_resources(self):
        print('Professor borrowla')
studentA=student('m','AS','55555')
studentB=student('f','sdsdsd','55123664')
ProfessorC=Professor('m','aasd','66659')
ProfessorD=Professor('f','ttttttt','7777777')



ls=[studentA,studentB,ProfessorC,ProfessorD]
for item in ls:
    item.borrow_resources()
studentA=student('m','IEM','B10721138')
print(studentA.get_gender())
studentA.set_gender('L')


