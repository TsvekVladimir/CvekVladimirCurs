import tkinter as tk
from GUI.setregistration import setregistr


def registr(connstud, cursor):
    regwindow = tk.Tk()
    regwindow.geometry("400x400")
    lblname = tk.Label(regwindow, text="Имя", padx=5, pady=5)
    lblname.pack()
    nameentr = tk.Entry(regwindow)
    nameentr.pack()
    lblsname = tk.Label(regwindow, text="Фамилия", padx=5, pady=5)
    lblsname.pack()
    sname = tk.Entry(regwindow)
    sname.pack()
    lbllname = tk.Label(regwindow, text="Отчество", padx=5, pady=5)
    lbllname.pack()
    lname = tk.Entry(regwindow)
    lname.pack()
    lblgrp = tk.Label(regwindow, text="Группа", padx=5, pady=5)
    lblgrp.pack()
    grp = tk.Entry(regwindow)
    grp.pack()
    btn = tk.Button(regwindow, text="Зарегистрироваться", command=lambda: setregistr(nameentr, sname, lname, grp,
                                                                                     connstud, cursor, regwindow))
    btn.pack()
