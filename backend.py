import sqlite3


class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS booklist (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        self.conn.commit()


    def insert(self,Title,Author,Year,ISBN):

        self.cur.execute("INSERT INTO booklist VALUES (NULL,?,?,?,?)",(Title, Author,Year,ISBN))
        self.conn.commit()


    def view(self):

        self.cur.execute("SELECT * FROM booklist")
        rows=self.cur.fetchall()
        return rows

    def search(self,Title="",Author="",Year="",ISBN=""):

        self.cur.execute("SELECT * FROM booklist where Title=? or Author=? or Year=? or ISBN=?",(Title,Author,Year,ISBN))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):

        self.cur.execute("DELETE FROM booklist where id=?",(id,))
        self.cur.execute("UPDATE booklist SET id=id-1 WHERE id>?",(id,))
        self.conn.commit()



    def update(self, id,Title,Author,Year,ISBN):

        self.cur.execute("UPDATE booklist SET Title=?,Author=?, Year=?, ISBN=? where id=?", (Title,Author,Year,ISBN,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


    # connect()
    # insert("Fargo","Unknown",1971,232113443321223)
    # insert("IT","Stephen king",1986,2321134433212553)
    # insert("The Shining","Stephen king",1977,23211344337483)
    # delete(1)
    # update(2,"The Fargo","ukw",1987,182893433)
    # print(view())
    # print(search(Author="Stephen king"))
