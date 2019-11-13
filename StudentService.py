from StudentList import StudentList
from copy import deepcopy

class StudentService():
     
    __sList = StudentList()

    def makeBackup(self):
        self.__sList.makeBackup()


    def restoreBackup(self):
        self.__sList.restoreBackup()


    def add(self, id_, name_, group_):
        self.__sList.add(id_, name_, group_)

    def init(self):
        self.__sList.makeBackup()
        self.add(1,"Andrei", 915)
        self.add(2,"Andreea", 912)
        self.add(3,"Beni", 915)
        self.add(4,"Mircea", 911)
        self.add(5,"Dan", 915)
        self.add(6,"Alexandra", 911)
        self.add(7,"Daria", 915)
        self.add(8,"Darius", 915)
        self.add(9,"Rares", 912)
        self.add(10,"Tudor", 912)
        self.__sList.makeBackup()

    def deleteByGroup(self, group_):  
         self.__sList.deleteByGroup(group_)

    def getData(self): 
        return self.__sList.getData()
    
