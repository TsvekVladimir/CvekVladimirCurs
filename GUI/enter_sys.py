import tkinter as tk
import tkinter.messagebox as mb
from database.server import connstud, cursor


def insys(nameentr, surnameentr, groupsenter):
    nameget = nameentr.get()
    surnameget = surnameentr.get()
    groupsget = groupsenter.get()
    cursor.execute("""SELECT * FROM student WHERE name = ? AND surname = ? AND groups = ?""", (nameget,
                                                                                               surnameget,
                                                                                               groupsget))
    std = cursor.fetchone()
    print(std)
    if std is None:
        msg = "Такой учетной записи не существует"
        mb.showinfo("Информация", msg)
        print(std)
    else:
        insyswindow = tk.Tk()
        std = std[0], std[1], std[2], std[3]
        lbl = tk.Label(insyswindow, text="Вы студент {} {} {} {}".format(std[0], std[1], std[2], std[3]))
        lbl.grid(column=0, row=0)



