import sqlite3

class AdminRepository:
    def save(self, admin):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute(
            """insert into admins
                (code, name, family, email, username, password, locked)
            values
                (?,?,?,?,?,?,?)""",
            [admin.code, admin.name, admin.family, admin.email, admin.username, admin.password, admin.locked])
        connection.commit()
        cursor.close()
        connection.close()

    def edit(self, admin):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, code):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        connection.commit()
        cursor.close()
        connection.close()


    def find_all(self):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cursor.close()
        connection.close()

    def find_by_code(self, code):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cursor.close()
        connection.close()

    def find_by_name_family(self, name, family):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cursor.close()
        connection.close()

    def find_by_username(self, username):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cursor.close()
        connection.close()

    def find_by_username_and_password(self, username, password):
        connection = sqlite3.connect('store.db.sqlite')
        cursor = connection.cursor()
        cursor.execute("SQL", [data])
        cursor.close()
        connection.close()