import tkinter as tk
from PIL import ImageTk,Image
import sqlite3

root = tk.Tk()
root.title("Database")
root.iconbitmap("./icon.ico")
root.geometry("400x400")

# Database

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

# Create table
#c.execute("""CREATE TABLE addresses (
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        state text,
#        zipcode integer
#    )""")

# Create delete records

def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Delete record
    c.execute("DELETE from addresses WHERE oid= " + str(delete_box.get()))
    
    # Commit Changes
    conn.commit()

    # Close connection
    conn.commit()

# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
            {
                "f_name": f_name.get(),
                "l_name": l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
            })

    # Commit Changes
    conn.commit()

    # Close connection
    conn.commit()

    # Clear the Text Boxes
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)

# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    
    # Loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Create Text Boxes
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1)
state = tk.Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = tk.Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = tk.Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = tk.Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = tk.Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = tk.Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = tk.Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = tk.Label(root, text="ID Number")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = tk.Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)

# Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=138)

# Create Delete Button
delete_btn = tk.Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()

#https://www.youtube.com/watch?v=c9_gcIeAru0&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=21
#7:48