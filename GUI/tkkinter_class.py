import tkinter as tk
import tkinter.messagebox as mb
from database.server import connstud, cursor
from GUI.enter_sys import insys
from GUI.registration import registr


class Loginwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        Loginwindow.title(self, "Программа студентов")
        Loginwindow.geometry(self, "700x700")
        enterlbl = tk.Label(self, text="Добро пожаловать!", padx=5, pady=5)
        enterlbl.pack()
        namelbl = tk.Label(self, text="Имя", padx=5, pady=5)
        namelbl.pack()
        nameentr = tk.Entry(self)
        nameentr.pack()
        surnamelbl = tk.Label(self, text="Фамилия", padx=5, pady=5)
        surnamelbl.pack()
        surnameentr = tk.Entry(self)
        surnameentr.pack()
        groupslbl = tk.Label(self, text="Группа", padx=5, pady=5)
        groupslbl.pack()
        groupsentr = tk.Entry(self)
        groupsentr.pack()

        enterbtn = tk.Button(self, text="Вход", command=lambda: insys(nameentr, surnameentr, groupsentr))
        enterbtn.pack()
        regbtn = tk.Button(self, text="Регистрация", command=lambda: registr(connstud, cursor))
        regbtn.pack()

    # def show_info(self):
    #     msg = "Ваши настройки сохранены"
    #     mb.showinfo("Информация", msg)
    #
    # def show_warning(self):
    #     msg = "Временные файлы удалены не правильно"
    #     mb.showwarning("Предупреждение", msg)
    #
    # def show_error(self):
    #     msg = "Приложение обнаружило неизвестную ошибку"
    #     mb.showerror("Ошибка", msg)


if __name__ == "__main__":
    app = Loginwindow()
    app.mainloop()