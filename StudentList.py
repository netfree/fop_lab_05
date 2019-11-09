from Student import Student
import copy

class StudentList():
    
    __l = []

    def __init__(self):
        pass

    def valid_id(self, id_):
        for s in self.__l:
            if s.id == id_:
                return False
        return True

    def add(self, id_, name_, group_):  
        new_student = Student(id_, name_, group_)
        
        if self.valid_id(new_student.id):
            self.__l.append(new_student)
        else:
            print(new_student.id)
            raise Exception("id taken")

    def deleteByGroup(self, group):
        Student(group=group)
        
        new_list = []

        for s in self.__l:
            if s.group != group:
                new_list.append(s)
        
        self.__l = copy.deepcopy(new_list)
        

    def getData(self):
        ans_list = []
        for s in self.__l:
            ans_list.append(s.getData())
        return ans_list

    

