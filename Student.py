class Student:
    __name = ""
    __id = 0
    __group = 0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("string expected")
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise Exception("int expected")
        else:
            self.__id = id
    
    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, group):
        if not isinstance(group, int):
            raise Exception("int expected")
        if group < 0:
            raise Exception("positive numeber expected")
        else:
            self.__group = group


    def __init__(self, id = 0, name = "", group = 0):
        self.id = id
        self.name = name
        self.group = group

