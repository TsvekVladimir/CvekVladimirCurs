import sqlite3

connstud = sqlite3.connect("../server/students.db")
cursor = connstud.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fname TEXT, 
                surname TEXT, 
                lastname TEXT, 
                groups TEXT
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS marks(
                id_stud,
                mark, 
                gpa 
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS admins(
                fname TEXT, 
                surname TEXT, 
                lastname TEXT, 
                groups TEXT,
                admin_token INT
                )""")
cursor.execute("""INSERT INTO admins VALUES (?, ?, ?, ?, ?)""", ("admin", "abcd1234", "adminov", "admins"
                                                                               , 1))
cursor.execute("""SELECT mark, gpa  
FROM marks LEFT JOIN student 
ON marks.id_stud = student.id;""")

connstud.commit()

