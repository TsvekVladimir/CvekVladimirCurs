from database.server import connstud, cursor

def setmrk(entr, entr1):
    idstd = entr.get()
    mark = entr1.get()
    cursor.execute("""INSERT INTO marks(mark, id_stud) VALUES (?, ?)""", (mark, idstd))
    cursor.execute("""SELECT * FROM marks WHERE id_stud = ?""", (idstd))
    print(cursor.fetchone())
