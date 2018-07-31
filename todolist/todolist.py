from datetime import datetime
from prettytable import PrettyTable
import dateparser

class task:
    def __init__(self, name_in, 
            priority_in=0, due_date_in=datetime.max):
        #poor style, change later 
        self.id = my_todo.idCount
        self.name = name_in
        if (due_date_in == datetime.max):
            self.due_date = due_date_in
        else:
            self.due_date = dateparser.parse(due_date_in)
        self.created = datetime.now()
        self.priority = priority_in

class todo_manager:
    def __init__(self):
        self.idCount = 0
        self.tasks = []

    def add_task(self, task):
        self.idCount += 1
        self.tasks.append(task)

    def display_tasks(self):
        #print output 
        output = PrettyTable()
        output.field_names = [ "ID", "NAME", "DUE", "PRIORITY", "CREATED"]
        for task in self.tasks:
            output.add_row([task.id, task.name, 
                task.due_date.strftime("%a, %d %b %Y"),
                task.priority, task.created.strftime("%d %b %Y")])
        print (output)
        
# idCount = 1
my_todo = todo_manager()
task_one = task('Task 1', due_date_in="July 5 2019")
# tasks = []
my_todo.add_task(task_one)
my_todo.add_task(task('Task 2'))
# tasks.append(task_one)
# tasks.append(task('Task 2'))

my_todo.display_tasks()
