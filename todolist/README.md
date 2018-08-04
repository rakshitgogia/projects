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

 ```