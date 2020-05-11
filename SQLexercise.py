import sqlite3


def create_table():
    conn = sqlite3.connect("prac.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price FLOAT)")
    conn.commit()
    conn.close()


create_table()


def insert(item, quantity, price):
    conn = sqlite3.connect("prac.db")
    cur = conn.cursor()
    # We should not use python placeholders here bc they are prone to SQL injections in the web
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("prac.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("prac.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = sqlite3.connect("prac.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()

# insert("Coffee Mug", 10, 20.0)
# insert("Tea Mug", 10, 20.0)
# insert("Whiskey Mug", 10, 20.0)

#delete('Coffee Mug')


update(15, 24.0, 'Tea Mug')
print(view())
