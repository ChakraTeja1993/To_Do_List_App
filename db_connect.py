import mysql.connector


try:
    db = mysql.connector.connect(
    username = "root",
    password = "password",
    host = "localhost",
    database = "mydatabase"
)
except mysql.connector.Error as e:
    print(f"Error connecting to database:{e}")

cursor = db.cursor()
def db_user_register_data(username,phonenumber,salt,hash_password,event_datetime):
    #updating the new user data
    insert_query = "INSERT INTO toDoListUserData (username,phonenumber,salt,hash_password,event_datetime) values(%s,%s,%s,%s,%s)"
    inser_data = (username,phonenumber,salt,hash_password,event_datetime)
    cursor.execute(insert_query,inser_data)
    #creating a new table users private data
    create_table_query = """CREATE TABLE {} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(255),
        description VARCHAR(255),
        event_datetime DATETIME)""".format(username)
    cursor.execute(create_table_query)
    db.commit()
    cursor.close()
    db.close()

def db_fetch_usercredentials(username):
    insert_query = "SELECT hash_password FROM toDoListUserData WHERE username = %s"
    cursor.execute(insert_query,(username,))
    global stored_hash_password
    stored_hash_password = cursor.fetchone()
    cursor.close()
    db.close()

def db_push_task(username,task_entered,description_entered,event_datetime):
    insert_query = "INSERT INTO {} (task,description,event_datetime) values(%s,%s,%s)".format(username)
    insert_data = (task_entered,description_entered,event_datetime)
    cursor.execute(insert_query,insert_data)
    db.commit()

def db_fetch_all_tasks(username):
    cursor = db.cursor()
    insert_query = "SELECT * FROM {}".format(username)
    cursor.execute(insert_query)
    global fetch_data
    fetch_data = cursor.fetchall()
    db.commit()
    
    
    