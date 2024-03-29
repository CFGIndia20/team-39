import sqlite3

class User :
    def __init__ (self, _id,username,password,email):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(row[0],row[1],row[2],row[3])
        else:
            user = None


        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(row[0],row[1],row[2],row[3])
        else:
            user = None

        connection.close()
        return user