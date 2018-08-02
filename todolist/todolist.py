from datetime import datetime
from prettytable import PrettyTable
import dateparser
import sqlite3
import argparse

conn = sqlite3.connect('log.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()


class task:
    def __init__(self, name_in,
                 priority_in, due_date_in):
        self.name = name_in
        if (due_date_in == ""):
            self.due_date = datetime.max
        else:
            self.due_date = dateparser.parse(due_date_in)
        self.created = datetime.now()
        self.priority = priority_in


class todo_manager:
    def __init__(self):
        self.initialise()

    def parse_args(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Make your todo-list from the command line')
        parser.add_argument('-n', '--name',
                            metavar='"TASK NAME"',
                            help='Create a new todo')
        parser.add_argument('-p', '--priority',
                            type=int,
                            default=0,
                            help='Create a new todo')
        parser.add_argument('-u', '--due',
                            metavar='"TASK NAME"',
                            default="",
                            help='Create a new todo')
        parser.add_argument('-d', '--done',
                            metavar='TASK_NUMBER',
                            type=int,
                            help='Mark task as done')
        parser.add_argument('-e', '--edit',
                            metavar='TASK_NUMBER',
                            type=int,
                            help='Edit task with new name, priority or due date')
        parser.add_argument('-cl', '--clear',
                            action='store_true',
                            help='Clear all todos')

        args = parser.parse_args()
        if (args.due or args.priority) and not args.name:
            print("Please provide a name for your task")
            exit(1)
        if args.edit:
            if not (args.name or args.priority or args.due):
                print("Please provide a new name, priority or due date "
                      "to edit your current task with")
                exit(1)
            print("Edited task number {}".format(args.edit))
            if args.name:
                self.edit_task_name(args.name, args.edit)
                print("New name: {}".format(args.name))
            if args.priority:
                self.edit_task_priority(args.priority, args.edit)
                print("New priority: {}".format(args.priority))
            if args.due:
                new_due_date = self.edit_task_due_date(args.due, args.edit)
                print("New due date: {}".format(
                    new_due_date.strftime("%d %b %Y")))
        elif args.name:
            taskname = ''.join(args.name)
            self.add_task(task(taskname, args.priority, args.due))
            print("Added \"{}\" to your todo-list".format(taskname))

        if args.done:
            print("Completed task {}: {}".format(args.done,
                                                 self.get_task(args.done)))
            self.delete_task(args.done)
        if args.clear:
            self.clear_all()
            print("Cleared all your todos")

    def initialise(self):
        c.execute("CREATE TABLE IF NOT EXISTS tasks "
                  "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                  "name TEXT, priority INT, "
                  "due_date TIMESTAMP, created TIMESTAMP)")

    def add_task(self, task):
        c.execute(
            "INSERT INTO tasks (name,priority,due_date,created) "
            "VALUES (?, ?, ?, ?)",
            (task.name, task.priority, task.due_date, task.created))

    def display_tasks(self):
        # print output in pretty table format
        output = PrettyTable()
        output.field_names = ["ID", "NAME", "PRIORITY", "DUE", "CREATED"]
        c.execute("SELECT * FROM tasks "
                  "ORDER BY priority DESC, due_date ASC, created DESC")
        log_output = c.fetchall()
        for row in log_output:
            output.add_row([row[0], row[1], row[2],
                            row[3].strftime("%a, %d %b %Y"),
                            row[4].strftime("%d %b %Y")])

        print(output)

    def delete_task(self, input_id):
        c.execute("DELETE FROM tasks "
                  "WHERE id = ?", (input_id,))

    def clear_all(self):
        c.execute("DROP TABLE tasks")
        self.initialise()

    def get_task(self, input_id):
        c.execute("SELECT name FROM tasks "
                  "WHERE id = ?", (input_id,))
        log_output = c.fetchone()
        if log_output:
            return log_output[0]
        else:
            print("Invalid task id")
            exit(1)

    def edit_task_name(self, name_in, row):
        c.execute("UPDATE tasks "
                  "SET name = ?"
                  "WHERE id = ?", (name_in, row))

    def edit_task_priority(self, priority_in, row):
        c.execute("UPDATE tasks "
                  "SET priority = ?"
                  "WHERE id = ?", (priority_in, row))

    def edit_task_due_date(self, due_date_in, row):
        new_due_date = dateparser.parse(due_date_in)
        c.execute("UPDATE tasks "
                  "SET due_date = ?"
                  "WHERE id = ?", (new_due_date, row))
        return new_due_date


my_todo = todo_manager()
my_todo.parse_args()
my_todo.display_tasks()

# save and quit
conn.commit()
conn.close()
