import sqlite3 

conn = sqlite3.connect("./../../db.sqlite3")
cursor = conn.cursor()

cursor.execute("INSERT INTO main_carnumbers VALUES (3,'one', 'two', 'three', 'four')")
conn.commit()

conn.close()
