from datetime import datetime, time
import csv
 
# Current date time in local system
startA = datetime.now()
print(startA)
 
# Name of the task taken
task_Name = input("\nWhat is the name of the task: \t")
#print(task_Name, "is the task name.")
 
#Task type
task_Type = input("\nWhich type of task is it: \t")
#print("\nThis is a", task_Type, "task type.")
 
# Name of user
user_Name = input("\nWhat is your name: \t")