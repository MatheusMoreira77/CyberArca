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

    website = input("Chose the website number to copy the password: ")
    cur.execute("SELECT id, website FROM users")
    results = cur.fetchall()

    if results:
        for row in results:
            print(f"{row[0]} - {row[1]}")
        website_id = input("Enter the website ID to copy the password: ")
        cur.execute("SELECT password_hash FROM users WHERE id = ?", (website_id,))
        result = cur.fetchone()
        if result:
            password_hash = result[0]
            print(f"Password for {website} copied to clipboard.")
    else:
        print("Website not found.")

    con.close()