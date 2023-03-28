import tkinter as tk
import tkinter.messagebox as mb
from database.server import connstud, cursor
from GUI.admin import adminka


def insys(nameentr, surnameentr, groupsenter):
    nameget = nameentr.get()
    surnameget = surnameentr.get()
    groupsget = groupsenter.get()
    cursor.execute("""SELECT * FROM student WHERE fname = ? AND surname = ? AND groups = ?""", (nameget,
                                                                                               surnameget,
                                                                                               groupsget))

    std = cursor.fetchone()
    cursor.execute("""SELECT * FROM admins WHERE fname = ? AND surname = ? AND groups = ? AND admin_token = ?""",
                           (nameget,
                            surnameget,
                            groupsget, 1))
    admin = cursor.fetchone()
    print(std)
    if std or admin is None:
        msg = "Такой учетной записи не существует"
        mb.showinfo("Информация", msg)
        print(std)
    elif admin:
        adminka()
    else:
        insyswindow = tk.Tk()
        insyswindow.title("Студент")
        insyswindow.geometry("300x300")
        std = std[0], std[1], std[2], std[3]
        lbl = tk.Label(insyswindow, text="Вы студент {} {} {} {}".format(std[0], std[1], std[2], std[3]))
        lbl.grid(column=0, row=0)




