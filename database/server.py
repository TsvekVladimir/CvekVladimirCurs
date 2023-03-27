import sqlite3

connstud = sqlite3.connect("../server/students.db")
cursor = connstud.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS student(
                name TEXT, 
                surname TEXT, 
                lastname TEXT, 
                groups TEXT
                )""")

connstud.commit()

