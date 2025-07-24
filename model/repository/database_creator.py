import sqlite3

connection = sqlite3.connect("store.db.sqlite")

# cursor = connection.cursor()

# cursor.execute("SQL")

# connection.commit()

# cursor.close()
connection.close()
