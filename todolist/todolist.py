from datetime import datetime
from prettytable import PrettyTable
import dateparser
import sqlite3

conn = sqlite3.connect('log.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()

# Create table if one does not already exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks
                     (id INT, name TEXT, due_date TIMESTAMP, priority INT, created TIMESTAMP)''')


class task:
    def __init__(self, name_in,
                 priority_in=0, due_date_in=datetime.max):
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

    def add_task(self, task):
        self.idCount += 1
        c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?)",
                  (task.id, task.name,
                   task.due_date,
                   task.priority, task.created))

    def display_tasks(self):
        # print output
        output = PrettyTable()
        output.field_names = ["ID", "NAME", "DUE", "PRIORITY"
            , "CREATED"]
        c.execute("SELECT * FROM tasks")
        log_output = c.fetchall()
        for row in log_output:
            output.add_row([row[0], row[1], row[2].strftime("%a, %d %b %Y"), row[3], row[4].strftime("%d %b %Y")])

        print(output)

    def clear_all(self):
        c.execute("DELETE FROM tasks")


my_todo = todo_manager()
task_one = task('Task 1', due_date_in="July 5 2019")
my_todo.add_task(task_one)
my_todo.add_task(task('Task 2'))
my_todo.add_task(task('Task 3', priority_in=3))
my_todo.clear_all()
my_todo.display_tasks()

# save and quit
conn.commit()
conn.close()