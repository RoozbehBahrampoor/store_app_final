import sqlite3

DB_PATH = "shop_data.db"

def get_all_houses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM houses")
    houses = cursor.fetchall()
    conn.close()
    return houses

def add_house(area, address, year_built, meterage, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO houses (area, address, year_built, meterage, price) VALUES (?, ?, ?, ?, ?)",
        (area, address, year_built, meterage, price)
    )
    conn.commit()
    conn.close()

def update_house(house_id, area, address, year_built, meterage, price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE houses SET area=?, address=?, year_built=?, meterage=?, price=? WHERE id=?",
        (area, address, year_built, meterage, price, house_id)
    )
    conn.commit()
    conn.close()

def delete_house(house_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM houses WHERE id=?", (house_id,))
    conn.commit()
    conn.close()
