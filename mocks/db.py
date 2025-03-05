import sqlite3

def save_user(name,age):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?)", (name, age))
    connection.commit()
    connection.close()