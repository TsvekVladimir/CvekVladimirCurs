import tkinter as tk
import tkinter.messagebox as mb


def setregistr(nameentr, sname, lname, grp, connstud, cursor, regwindow):
    name = nameentr.get()
    surname = sname.get()
    lastname = lname.get()
    group = grp.get()
    cursor.execute("""INSERT INTO student VALUES (?, ?, ?, ?);""", (name, surname, lastname, group))
    connstud.commit()
    msg = "Ваши данные сохранены"
    mb.showinfo("Информация", msg)
    regwindow.destroy()
