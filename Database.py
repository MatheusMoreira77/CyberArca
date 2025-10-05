import sqlite3
import random
import string
import hashlib
import pyperclip

caracter_pool = string.ascii_letters + string.digits + string.punctuation

def Conexao():
    con = sqlite3.connect('Ark.db')

    cur = con.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        website TEXT NOT NULL,
        email TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    con.commit()
    con.close()

def adcionar():
    con = sqlite3.connect('Ark.db')
    cur = con.cursor()

    website = input("Enter website: ")
    email = input("Enter email: ")
    password = input("Do you want a random password? (y/n): ")
    if password.lower() == 'y':
        password = ''.join(random.choices(caracter_pool, k=12))
        print("Generated password: {password}")
    else:
        password = input("Enter password: ")
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()


    cur.execute("INSERT INTO users (website, email, password_hash) VALUES (?, ?, ?)", (website, email, password_hash))

    con.commit()
    con.close()
    print("User added successfully.")


def Copy_password():
    con = sqlite3.connect('Ark.db')
    cur = con.cursor()
    cur.execute("SELECT id, website FROM users")
    all_entries = cur.fetchall()

    if not all_entries:
        print("No entries found.")
        return

    print("Select an entry to copy the password:")
    for entry in all_entries:
        print(f"{entry[0]}: {entry[1]}")
    entry_id = input("Enter the ID of the entry: ")
    cur.execute("SELECT password_hash FROM users WHERE id = ?", (entry_id,))
    result = cur.fetchone()
    if result:
        password_hash = result[0]
        password = hashlib.sha256(password_hash.encode()).hexdigest()
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    else:
        print("Entry not found.")

    con.close()