from StudentService import StudentService

class UI:

    s_srv = StudentService()
    s_srv.init()

    def printList(self):
        data = self.s_srv.getData()
        for dataRow in data:
            print(dataRow)

    def start(self):
        while True:
            print("Choose action: 1.add 2.print 3.deleteByGroup 4. undo")
            action = input(">>>")

            if(action == "exit"):
                break

            try:
                action = int(action)
            except Exception as ex:
                print("invalid command")
                continue
            try:
                
                if action == 1:
                    id = int(input("id: "))
                    name = input("name: ")
                    group = int(input("group: "))
                    self.s_srv.makeBackup()
                    self.s_srv.add(id, name, group)

                elif action == 2:
                    self.printList()

                elif action == 3:
                    group = int(input("group:"))
                    self.s_srv.makeBackup()
                    self.s_srv.deleteByGroup(group)
                elif action == 4:
                    self.s_srv.restoreBackup()

                
            except Exception as ex:
                print(str(ex))

