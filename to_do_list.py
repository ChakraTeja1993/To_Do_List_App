import db_connect
import datetime
username = "chakra"
MAX_CHARACTERS = 255

def to_do_list():
   while True:
      
      user_input = input("Please enter your preference\n 1.add task 2.show all tasks 3.delete task 4.exit\n")

      if user_input == str(1): 
            while True:
                task_entered = input("please enter your task here\n")
                description_entered = input("please enter the task description\n")
                event_datetime = datetime.datetime.now()

                if 0 != len(task_entered) <= MAX_CHARACTERS and 0 != len(description_entered) <= MAX_CHARACTERS:
                     try:
                       db_connect.db_push_task(username,task_entered,description_entered,event_datetime)
                       print("Task updated succesfully")
                       break
                     except db_connect.mysql.connector.Error as e:
                       print(f"error connecting to database: {e}")
                else: print("chatacter limit for task and description is 255 and should not be empty. please try again\n")

      elif user_input == str(2):
           try:
              db_connect.db_fetch_all_tasks(username)
           except db_connect.mysql.connector.Error as e:
               print(f"Error fetching data: {e}")
           for task in db_connect.fetch_data:
               print(f"task{task[0]-1}: {task[1]}, Description: {task[2]}")

      elif user_input == str(4):
          db_connect.cursor.close()
          db_connect.db.close()
          break
           
               

to_do_list()
