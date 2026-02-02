import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()
print("Database connected successfully!")
def show_all():
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
#Query to the datrabase
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
print("Name\t\t Last Name \t Email")
print("-------------------------------------------")
for item in items:
    print(f"{item[0]}\t\t {item[1]}\t\t {item[2]}")
print("All tuple items data fetched successfully")