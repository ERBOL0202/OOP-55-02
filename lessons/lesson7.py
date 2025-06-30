import sqlite3

# A4 - бумага
connect = sqlite3.connect("users.db")
# Рука с карандашом
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        brand_name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')