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
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )""")

# Commit Changes
conn.commit()

# Close connection
conn.commit()

root.mainloop()