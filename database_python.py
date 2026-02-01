import sqlite3
import os

# Remove corrupted database if it exists
if os.path.exists('customer.db'):
    os.remove('customer.db')
    print("Old database removed")

try:
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    print("Database connected successfully!")
    
    #Create a table
    c.execute("""
                CREATE TABLE IF NOT EXISTS customers(
              fist_name text,
              last_name text,
              email text
     ) """)
    print("Table created/verified successfully")

    #Insert a record
    c.execute("INSERT INTO customers VALUES ('Sovan', 'Rajbanshi', 'pwangdu323@gmail.com')")
    print("Record inserted successfully")
    c.execute("INSERT INTO customers VALUES ('Shubham', 'Kumar', 'shubhamkumar@gmail.com')")
    print("Record inserted successfully")
    # the table addding many records
    many_customers = [
        ('John', 'Doe', 'john.doe@example.com'),
        ('Jane', 'Smith', 'jane.smith@example.com'),
        ('Bob', 'Johnson', 'bob.johnson@example.com')
    ]
    c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
    print ("Multiple values are added successfully")

    # The fetching command in sqllite
    c.execute("SELECT * FROM customers")
    print(c.fetchone())
    print(c.fetchmany(3))
    print(c.fetchall())
    print("Data fetched successfully")
    # commit or command
    conn.commit()
    print("Data committed to database")

    #Close our connection
    conn.close()
    print("Connection closed")

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Error: {e}")