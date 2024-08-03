class ToDoList:
    def __init__(self) -> None:
        self.tasks = []
        self.loop = True
    
    def addtasks(self):
        task = input("Enter the task: ")
        self.tasks.append([task, "progress"])
        print("---Task added successfully---")
    
    def viewtasks(self, category="All"):
        f = 0
        if category == "All":
            if len(self.tasks) > 0:
                f = 1
            for i in range(len(self.tasks)):
                print(f"[{i + 1}] => {self.tasks[i][0]} => {self.tasks[i][1]}")
        elif category == "progress":
            for i in range(len(self.tasks)):
                if self.tasks[i][1] == "progress":
                    print(f"[{i + 1}] => {self.tasks[i][0]}")
                    f = 1
        elif category == "completed":
            for i in range(len(self.tasks)):
                if self.tasks[i][1] == "completed":
                    print(f"[{i + 1}] => {self.tasks[i][0]}")
                    f = 1
        if f == 0:
            print("Nothing to display")
        return f
    
    def deletetask(self):
        if len(self.tasks) > 0:
            self.viewtasks()
            ind = int(input("Enter the index of the task: ")) - 1
            if len(self.tasks) < ind or ind < 0:
                print("The given index is out of range.")
                return
            else:
                self.tasks.pop(ind)
                print("---Task deleted successfully---")
        else:
            print("The list is empty. Nothing to delete.")
            return

    def markascomplete(self):
        if len(self.tasks) > 0:
            f = self.viewtasks("progress")
            if f:
                ind = int(input("Enter the index of the task: ")) - 1
                if len(self.tasks) < ind or ind < 0:
                    print("The given index is out of range.")
                    return
                else:
                    self.tasks[ind][1] = "completed"
                    print("---Task marked as completed successfully---")
        else:
            print("The list is empty. Nothing to update.")
            return
        
    def menu(self):
        print("-----Menu-----")
        print("""
[1] Add a Task
[2] Delete a Task
[3] Display all Tasks
[4] Display Tasks in Progress
[5] Display Tasks that are Completed
[6] Mark as Complete a Task
[7] Exit""")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            self.addtasks()
        elif ch == 2:
            self.deletetask()
        elif ch == 3:
            self.viewtasks()
        elif ch == 4:
            self.viewtasks("progress")
        elif ch == 5:
            self.viewtasks("completed")
        elif ch == 6:
            self.markascomplete()
        elif ch == 7:
            print("Closing...")
            self.loop = False
        else:
            print("The choice is not valid.")

obj = ToDoList()
while(obj.loop):
    obj.menu()