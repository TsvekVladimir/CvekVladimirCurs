import tkinter as tk
import tkinter.messagebox as mb
from database.server import connstud, cursor
from GUI.setmark import setmrk


def adminka():
    adminwindow = tk.Tk()
    adminwindow.title("Администратор аннигилятор")
    adminwindow.geometry("400x400")
    cursor.execute("""SELECT * FROM student""")
    studaki = cursor.fetchall()
    std = tk.Label(adminwindow, text=studaki)
    std.grid(row=0, column=0)
    entr = tk.Entry(adminwindow)
    entr.grid(row=1, column=0)
    entr1 = tk.Entry(adminwindow)
    entr1.grid(row=2, column=0)
    btn = tk.Button(adminwindow, text=("Поставить оценку"), command=lambda: setmrk(entr, entr1))
    btn.grid(row=3, column=0)


