from Student import Student
import copy

class StudentList():
    
    __l = []

    __bk = []

    def makeBackup(self):
        self.__bk.append(copy.deepcopy(self.__l))

    def restoreBackup(self):
        if len(self.__bk):
            self.__l[:] = self.__bk[-1][:]

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

    

