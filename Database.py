import sqlite3
import random
import string
import hashlib
import pyperclip
import getpass

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

def adicionar():
    con = sqlite3.connect('Ark.db')
    cur = con.cursor()

    website = input("Enter website: ")
    email = input("Enter email: ")
    password = input("Do you want a random password? (y/n): ")
    if password.lower() == 'y':
        password = ''.join(random.choices(caracter_pool, k=12))
        print("Generated password: {password}")
    else:
        password = getpass.getpass("Enter password: ")
    


    cur.execute("INSERT INTO users (website, email, password_hash) VALUES (?, ?, ?)", (website, email, password))

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
        password = result[0]

        pyperclip.copy(password)
        print("Password copied to clipboard.")
    else:
        print("Entry not found.")

    con.close()

def Editar():
    con = sqlite3.connect('Ark.db')
    cur = con.cursor()
    cur.execute("SELECT id, website FROM users")
    all_entries = cur.fetchall()

    if not all_entries:
        print("No entries found.")
        return

    print("Select an entry to edit:")
    for entry in all_entries:
        print(f"{entry[0]}: {entry[1]}")
    entry_id = input("Enter the ID of the entry: ")
    cur.execute("SELECT website, email, password_hash FROM users WHERE id = ?", (entry_id,))
    result = cur.fetchone()

    print("Leave a field blank to keep it unchanged.")
    new_website = input(f"New website (current: {result[0]}): ") or result[0]
    new_email = input(f"New email (current: {result[1]}): ") or result[1]
    new_password = getpass.getpass("New password (leave blank to keep current): ") or result[2]
    cur.execute("UPDATE users SET website = ?, email = ?, password_hash = ? WHERE id = ?", (new_website, new_email, new_password, entry_id))
    con.commit()
    con.close()
    print("Entry updated successfully.")

def Deletar():
    con = sqlite3.connect('Ark.db')
    cur = con.cursor()
    cur.execute("SELECT id, website FROM users")
    all_entries = cur.fetchall()

    if not all_entries:
        print("No entries found.")
        return

    print("Select an entry to delete:")
    for entry in all_entries:
        print(f"{entry[0]}: {entry[1]}")
    entry_id = input("Enter the ID of the entry: ")
    cur.execute("SELECT website, email FROM users WHERE id = ?", (entry_id,))
    result = cur.fetchone()
    if result:
        confirm = input(f"Are you sure you want to delete the entry for {result[0]} (email: {result[1]})? (y/n): ")
        if confirm.lower() == 'y':
            cur.execute("DELETE FROM users WHERE id = ?", (entry_id,))
            con.commit()
            print("Entry deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Entry not found.")

    con.close()
    
if __name__ == "__main__":
    Conexao()