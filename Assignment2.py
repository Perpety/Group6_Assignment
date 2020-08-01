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

#Program menu
def task_Menu():
    print("\n\t Welcome", user_Name, "to the Time Traker Program!")
    print("\nSelect an option: \t")
    print("Option [1] Calculate the date and time to complete the task.")
    print("Option [2] Quit ")

    option = int(input("Choose an option: \t"))
    if option == 1:
        convert_to_csv()
    else:
        exit(0)

#Gets task started datetime input from user
start = input("\nInput date and time you started the task in YYY-MM-DD (hh:mm): \t")
format = "%Y-%m-%d %H:%M"
start_time = datetime.strptime(start, format)

#Gets task ended datetime input from user 
end = input("\nInput date and time you ended the task in YYY-MM-DD (hh:mm): \t")
end_time = datetime.strptime(end, format)
print("\nYou started the task at", start_time, "and ended at", end_time)
       

def time_Spent():
    print("Acculating The time spent on task.")

        #Gets task started datetime input from user
    start = input("\nInput date and time you started the task in YYY-MM-DD (hh:mm): \t")
    format = "%Y-%m-%d %H:%M"
    start_time = datetime.strptime(start, format)

    #Gets task ended datetime input from user 
    end = input("\nInput date and time you ended the task in YYY-MM-DD (hh:mm): \t")
    end_time = datetime.strptime(end, format)
    print("\nYou started the task at", start_time, "and ended at", end_time)
        

    #Time spent on task
    diff_time = end_time - start_time
    print("\nYou spent", diff_time, "on the task.")

    #Extrat day and seconds from datetime 
    day = diff_time.days
    print(day)
    second = diff_time.total_seconds()
    print(second)

    #Convert the time spent to hours
    hours_spent = second / 3600
    print("\nYou spent", hours_spent, "hours on the task.")


    return hours_spent

def convert_to_csv():
    hours_spent = time_Spent()

    #Payment for an hour task is $5 dollars
    hour_payment = 5
    amount_earned = hours_spent * hour_payment
    print("\nYour total money earned is", amount_earned, "dollars.")
    print("Converting to) csv file.....")

    with open('TTT.csv', 'a', newline="") as csv_file:
        header = ['TYPE', 'Task Name', 'Date and Time Task Started', 'Date and Time Task Ended ',
            'Number of hours spent', 'Total money earned $']
        writer = csv.DictWriter(csv_file, fieldnames=header)

        data = {'TYPE': task_Type, 'Task Name': task_Name, 'Date and time task started': start_time,
            'Date and time task ended ': end_time, 'Number of hours spent': hours_spent,
            'Total money earned $': amount_earned}
        with open('TTT.csv', 'r') as reader:
            d_reader = csv.DictReader(reader)
            headers = d_reader.fieldnames
        if headers == None:
            writer.writeheader()
            writer.writerow(data)
        else:
            writer.writerow(data)

if __name__ == "__main__":
   task_Menu()


# You can run this to Tis is version 2
# Mine
from datetime import datetime, time
import csv

# Current date time in local system
startA = datetime.now()
print(startA)

# Name of the task taken
task_Name = input("What is the name of the task: \t")
print(task_Name, "is the task name.")

#Task type
task_Type = input("Which type of task is it: \t")
print("This is a", task_Type, "task type.")

# Name of user
user_Name = input 

#Program menu
def task_Menu():


def menu_options():
       print("*****************************************************")
   print("\tWelcome Time Tracking Program")
   print("*****************************************************")
   print("Enter the number to select an option:")
   print("[1] Calculate time taken to complete a task and export as csv")
   print("[2] Calculate time taken to complete a task and export as excel")
   print("[3] Quit")

   option = input("Option: ")
   option = int(option)    # convert option to an integer
   if option == 1:
       convert_to_csv()
   elif option == 2:
       convert_to_excel()
   else:

#Gets task started datetime input from user
start = input("Input time started the task in HH:MM: \t")
format = "%Y-%m-%d %H:%M:%S"
start_Time = datetime.strptime(start, format)

#Gets task ended datetime input from user 
end = input("Input time ended the task in : \t")
end_Time = datetime.strptime(end, format)
print("You started the task at", start_Time, "and ended at", end_Time)

#Time spent on task
diff_time = end_Time - start_Time
print("You spent", diff_time, "on the task.")

#Extrat days, hours, minutes and seconds from datetime 
day = diff_time.days
print(day)
second = diff_time.total_seconds()
print(second)

#Convert the time spent to hours
hours_spent = second // 3600
print("You spent", hours_spent, "hours on the task.")

#Amount earned after the task
#Payment for an hour task is $5 dollars
hour_payment = 5
amount_earned = hours_spent * hour_payment
print("Your total money earned is", amount_earned, "dollars.")

with open('TTT.csv', 'a', newline="") as csv_file:
    header = ['TYPE', 'Task Name', 'Time Task Started', 'Time Task Ended ',
        'Number of hours spent', 'Total money earned $']
    writer = csv.DictWriter(csv_file, fieldnames=header)
 
    data = {'TYPE': task_type, 'Task Name': task_Name, 'Time Task Started': start_Time,
        'Time Task Ended ': end_Time, 'Number of hours spent': hours_spent,
        'Total money earned $': amount_earned}
    with open('TTT.csv', 'r') as reader:
        d_reader = csv.DictReader(reader)
        headers = d_reader.fieldnames
    if headers == None:
        writer.writeheader()
        writer.writerow(data)
    else:
        writer.writerow(data)