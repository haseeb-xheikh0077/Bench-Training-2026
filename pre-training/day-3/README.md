I built a task tracker CLI that saves tasks to a tasks.json file so they survive between runs.

Commands i used:
python3 exercise_1.py add 'Fix login bug'
python3 exercise_1.py done 1
python3 exercise_1.py list
python3 exercise_1.py list --filter done
python3 exercise_1.py delete 2

Why i used classes instead of just functions:
The task list is shared state. Every operation like add, delete, complete all read and write the same list. With plain functions i would have to pass that list into every function manually. With a class the list lives in self.tasks and every method just uses it directly. Also loading the file once in __init__ means i dont have to remember to load before and save after every operation, the class handles that internally.
Task class is separate because it only cares about one task and how to convert itself to and from a dict for json. TaskManager only cares about the full list. Keeping them separate means if i add a new field to Task i only change it in one place.

Additional thing : I used os methods so that it can run from anywhere in the terminal.