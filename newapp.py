import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()

def show_all():
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
#add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # commit the changes
    conn.commit()
    # closing the connection
    conn.close()

# delete a record from the table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid=(?)", (id,))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

#look up with where clause
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE email=(?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.close()