# Todolist
By Rakshit Gogia

Version 1.0, 4 Aug 2018

Manage a todo list from the command line

## Requirements
You need to have the following
- [python3](https://www.python.org/downloads/)
- sqlite3 library
- dateparser library
- argparse library

## Usage:
todolist.py \[-h] \[-n "TASK NAME"] \[-p PRIORITY] \[-u DUE DATE]
                   \[-d TASK_NUMBER] \[-e TASK_NUMBER] \[-cl]

### optional arguments:
```
  -h, --help            show this help message and exit
  -n "TASK NAME", --name "TASK NAME"
                        Name of todo
  -p PRIORITY, --priority PRIORITY
                        Priority of todo
  -u DUE DATE, --due DUE DATE
                        Due date of todo
  -d TASK_NUMBER, --done TASK_NUMBER
                        Mark task as done
  -e TASK_NUMBER, --edit TASK_NUMBER
                        Edit task with new name, priority or due date
  -cl, --clear          Clear all todos
  ```

### examples:
 ```
python3 todolist.py -n "My first task"

Added "My first task" to your todo-list
+----+---------------+----------+------------------+-------------+
| ID |      NAME     | PRIORITY |       DUE        |   CREATED   |
+----+---------------+----------+------------------+-------------+
| 1  | My first task |    0     | Fri, 31 Dec 9999 | 04 Aug 2018 |
+----+---------------+----------+------------------+-------------+
 ```
 ```
python3 todolist.py -n "My second task" -u "Oct 20"

Added "My second task" to your todo-list
+----+----------------+----------+------------------+-------------+
| ID |      NAME      | PRIORITY |       DUE        |   CREATED   |
+----+----------------+----------+------------------+-------------+
| 2  | My second task |    0     | Sat, 20 Oct 2018 | 04 Aug 2018 |
| 1  | My first task  |    0     | Fri, 31 Dec 9999 | 04 Aug 2018 |
+----+----------------+----------+------------------+-------------+
 ```
 ```
python3 todolist.py -n "My third task" -u "Tomorrow" -p 3

Added "My third task" to your todo-list
+----+----------------+----------+------------------+-------------+
| ID |      NAME      | PRIORITY |       DUE        |   CREATED   |
+----+----------------+----------+------------------+-------------+
| 3  | My third task  |    3     | Sun, 05 Aug 2018 | 04 Aug 2018 |
| 2  | My second task |    0     | Sat, 20 Oct 2018 | 04 Aug 2018 |
| 1  | My first task  |    0     | Fri, 31 Dec 9999 | 04 Aug 2018 |
+----+----------------+----------+------------------+-------------+
```
```
python3 todolist.py -e 2 -p 5

Edited task number 2
New priority: 5
+----+----------------+----------+------------------+-------------+
| ID |      NAME      | PRIORITY |       DUE        |   CREATED   |
+----+----------------+----------+------------------+-------------+
| 2  | My second task |    5     | Sat, 20 Oct 2018 | 04 Aug 2018 |
| 3  | My third task  |    3     | Sun, 05 Aug 2018 | 04 Aug 2018 |
| 1  | My first task  |    0     | Fri, 31 Dec 9999 | 04 Aug 2018 |
+----+----------------+----------+------------------+-------------+
```
```
python3 todolist.py -d 1

Completed task 1: My first task
+----+----------------+----------+------------------+-------------+
| ID |      NAME      | PRIORITY |       DUE        |   CREATED   |
+----+----------------+----------+------------------+-------------+
| 2  | My second task |    5     | Sat, 20 Oct 2018 | 04 Aug 2018 |
| 3  | My third task  |    3     | Sun, 05 Aug 2018 | 04 Aug 2018 |
+----+----------------+----------+------------------+-------------+
```
```
python3 todolist.py -cl

Cleared all your todos
+----+------+----------+-----+---------+
| ID | NAME | PRIORITY | DUE | CREATED |
+----+------+----------+-----+---------+
+----+------+----------+-----+---------+
```