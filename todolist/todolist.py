from datetime import date, datetime
from prettytable import PrettyTable
import dateparser

class task:
    def __init__(self, name_in, 
            priority_in=0, due_date_in=datetime.max):
        #poor style, change later 
        global idCount
        self.id = idCount
        idCount += 1
        self.name = name_in
        if (due_date_in == datetime.max):
            self.due_date = due_date_in
        else:
            self.due_date = dateparser.parse(due_date_in)
        self.created = datetime.now()
        self.priority = priority_in
idCount = 1
task_one = task('Task 1', due_date_in="July 5 2019")
tasks = []
tasks.append(task_one)
tasks.append(task('Task 2'))
#print output 
output = PrettyTable()
output.field_names = ["ID", "NAME", "DUE", "PRIORITY", "DATE CREATED"]
for task in tasks:
    output.add_row([task.id, task.name, 
        task.due_date.strftime("%a, %d %b %Y"),
        task.priority, task.created.strftime("%d %b %Y")])

print (output)
