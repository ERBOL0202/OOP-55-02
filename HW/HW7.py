import sqlite3

connect = sqlite3.connect("HW7.db")
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        brand_name VARCHAR (100) NOT NULL,
        year_manufacture INTEGER NOT NULL,
        mileage REAL NOT NULL
    )
''')
connect.commit()
def add_cars(brand_name, year_manufacture, mileage):
    cursor.execute(
        'INSERT INTO cars(brand_name, year_manufacture, mileage) VALUES (?,?,?)',
        (brand_name, year_manufacture, mileage)
    )
    connect.commit()
def get_all_cars():
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    print(f"All cars: {cars}")
def update_cars(brand_name, rowid):
    cursor.execute(
        'UPDATE cars SET brand_name = ? WHERE rowid = ?',
        (brand_name, rowid)
    )
    connect.commit()
    print("cars updated")
def delete_cars(rowid):
    cursor.execute('DELETE FROM cars WHERE rowid = ?', (rowid,))
    connect.commit()
    print('cars deleted')