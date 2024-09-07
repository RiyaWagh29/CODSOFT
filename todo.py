class TodoList:
    tasks={}
    
    def display_tasks(self):
        print("To-do list:")
        for tasks,status in self.tasks.items():
            print(tasks,":",status)
            
    def add_task(self):
        task= input("Enter task:")
        self.tasks[task]="Not started"
        print("Task", task, "added!")
        
    def update_task(self):
        task = input("Enter task to update: ")
        if task in self.tasks:
            status = input("Enter new status: ")
            self.tasks[task]=status
            print("Task", task, "updated!")
        else:
            print("Task not found!")
            
    def delete_task(self):
        task = input("Enter task to delete: ")
        if task in self.tasks:
            del self.tasks[task]
            print("Task", task, "deleted!")
        else:
            print("Task not found!")
            
todo= TodoList()
while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    
    select=int(input("Enter your choice:"))
    if select==1:
        todo.display_tasks()
    elif select== 2:
        todo.add_task()
    elif select==3:
        todo.update_task()
    elif select== 4:
        todo.delete_task()
    elif select==5:
        break
    else:
        print("Invalid choice!")