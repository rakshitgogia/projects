from datetime import datetime
from prettytable import PrettyTable
import dateparser
import sqlite3


conn = sqlite3.connect('log.db')
c = conn.cursor()

# Create table if one does not already exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks
                     (id int, name text, due_date date, priority int, created date)''')
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
        self.idCount = 1
#         below is not needed
        self.tasks = []

    def add_task(self, task):
        self.idCount += 1
#         wouldnt need below line
        self.tasks.append(task)
        c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?)", 
        (task.id, task.name, 
            task.due_date.strftime("%a, %d %b %Y"), 
            task.priority, task.created.strftime("%d %b %Y")))
        conn.commit()

    def display_tasks(self):
        #print output 
        output = PrettyTable()
        output.field_names = [ "ID", "NAME", "DUE", "PRIORITY"
                , "CREATED"]
        c.execute("SELECT * FROM tasks")
        log_output = c.fetchall()
#         print(log_output)
        for row in log_output:
            output.add_row(row)
#         for task in self.tasks:
#             output.add_row([task.id, task.name, 
#                 task.due_date.strftime("%a, %d %b %Y"),
#                 task.priority, task.created.strftime("%d %b %Y")])
        print (output)
        
my_todo = todo_manager()
task_one = task('Task 1', due_date_in="July 5 2019")

my_todo.add_task(task_one)
my_todo.add_task(task('Task 2'))

my_todo.display_tasks()

conn.commit()
conn.close()
