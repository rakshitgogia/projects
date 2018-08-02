from datetime import datetime
from prettytable import PrettyTable
import dateparser
import sqlite3

conn = sqlite3.connect('log.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()

# Create table if one does not already exist


class task:
    def __init__(self, name_in,
                 priority_in=0, due_date_in=datetime.max):
        self.name = name_in
        if (due_date_in == datetime.max):
            self.due_date = due_date_in
        else:
            self.due_date = dateparser.parse(due_date_in)
        self.created = datetime.now()
        self.priority = priority_in


class todo_manager:
    def __init__(self):
        self.initialise()

    def initialise(self):
        c.execute('''CREATE TABLE IF NOT EXISTS tasks
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, due_date TIMESTAMP, priority INT, created TIMESTAMP)''')

    def add_task(self, task):
        c.execute(
            "INSERT INTO tasks (name,due_date,priority,created)"
            " VALUES (?, ?, ?, ?)",
            (task.name,
             task.due_date,
             task.priority, task.created))

    def display_tasks(self):
        # print output
        output = PrettyTable()
        output.field_names = ["ID", "NAME", "DUE", "PRIORITY"
            , "CREATED"]
        c.execute("SELECT * FROM tasks")
        c.execute("SELECT * FROM tasks"
                  " ORDER BY priority DESC, due_date ASC, created DESC")
        log_output = c.fetchall()
        for row in log_output:
            output.add_row(
                [row[0], row[1], row[2].strftime("%a, %d %b %Y"), row[3],
                 row[4].strftime("%d %b %Y")])

        print(output)

    def delete_task(self, input_id):
        c.execute("DELETE FROM tasks"
                  " WHERE id = ?", (input_id,))

    def clear_all(self):
        c.execute("DROP TABLE tasks")
        self.initialise()

my_todo = todo_manager()
task_one = task('Task 1', due_date_in="July 5 2019")
my_todo.add_task(task_one)
my_todo.add_task(task('Task 2'))
my_todo.add_task(task('Task 3', priority_in=3))
my_todo.delete_task(1)
my_todo.clear_all()
my_todo.display_tasks()

# save and quit
conn.commit()
conn.close()
