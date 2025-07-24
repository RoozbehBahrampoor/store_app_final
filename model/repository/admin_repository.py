import sqlite3


class AdminRepository:
    def connect(self):
        self.connection = sqlite3.connect("store.db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, admin):
        self.connect()
        self.cursor.execute(
            """insert into admins 
                   (code, name, family, email, username, password, locked)
               values (?, ?, ?, ?, ?, ?, ?)""",
            [admin.code, admin.name, admin.family, admin.email, admin.username, admin.password, admin.locked])
        self.disconnect(commit=True)

    def edit(self, admin):
        self.connect()
        self.cursor.execute("update admins set name=?, family=?, email=?, username=?, password=?, locked=?where code=?",
                            [admin.name, admin.family, admin.email, admin.username, admin.password, admin.locked,
                             admin.code])
        self.disconnect(commit=True)

    def delete(self, code):
        self.connect()
        self.cursor.execute("delete from admins where code = ?", [code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from admins")
        self.disconnect()
        return self.cursor.fetchall()

    def find_by_code(self, code):
        self.connect()
        self.cursor.execute("select * from admins where code = ?", [code])
        self.disconnect()
        return self.cursor.fetchone()

    def find_by_name_family(self, name, family):
        self.connect()
        self.cursor.execute("select * from admins where name like ? and family like ?", [name + "%", family + "%"])
        self.disconnect()
        return self.cursor.fetchall()

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from admins where username = ?", [username])
        self.disconnect()
        return self.cursor.fetchone()

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from admins where username = ? and password = ?", [username, password])
        self.disconnect()
        return self.cursor.fetchone()
