
from collections import deque

task_manager = deque()
#add tasks at the end of the queue
task_manager.append("task1")
task_manager.append("task2")
task_manager.append("task3")

print("Task in the manager:")
for task in task_manager:
    print(task)

#Remove tasks from the front of the list.
task_manager.popleft()

print("\nTask in the manager after removing one task:")
for task in task_manager:
    print(task)

#Rotate tasks if a task gets postponed.
task_manager

print("\nTask in the manager after rotating:")
for task in task_manager:
    print(task)
    