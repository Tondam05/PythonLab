# QUESTION NO:3
class todoReminder:
    def __init__(self):
        self.todo = []

    def list_todo(self):
        print(" the following are the list of TODO items")

        for i in range(len(self.todo)):
            print("%r : %s" %(i, self.todo[i]))

    def new_todo(self, item):
        self.todo.append(item)

    def remove_todo(self, i):
        del (self.todo[i])

T = todoReminder()
T.new_todo("wake up at 6")
T.new_todo("we are going to submit friday")
T.new_todo("its time to python lab")
T.new_todo("check the questions once again")
T.list_todo()
T.remove_todo(1)
T.list_todo()