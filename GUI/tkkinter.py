import tkinter as tk
from GUI.enter_sys import insys
from GUI.registration import registr
from database.server import connstud, cursor

loginwindow = tk.Tk()
loginwindow.title("Программа студентов")
loginwindow.geometry("700x700")

enterlbl = tk.Label(loginwindow, text="Добро пожаловать!", padx=5, pady=5)
enterlbl.pack()
namelbl = tk.Label(loginwindow, text="Имя", padx=5, pady=5)
namelbl.pack()
nameentr = tk.Entry()
nameentr.pack()
surnamelbl = tk.Label(loginwindow, text="Фамилия", padx=5, pady=5)
surnamelbl.pack()
surnameentr = tk.Entry()
surnameentr.pack()
groupslbl = tk.Label(loginwindow, text="Группа", padx=5, pady=5)
groupslbl.pack()
groupsentr = tk.Entry()
groupsentr.pack()

enterbtn = tk.Button(loginwindow, text="Вход", command=lambda: insys(nameentr, surnameentr, groupsentr))
enterbtn.pack()
regbtn = tk.Button(loginwindow, text="Регистрация", command=lambda: registr(connstud, cursor))
regbtn.pack()

loginwindow.mainloop()



# if __name__ == '__main__':
