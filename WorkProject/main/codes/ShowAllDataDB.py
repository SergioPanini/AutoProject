import sqlite3 

conn = sqlite3.connect("./../../db.sqlite3")
cursor = conn.cursor()

cursor.execute("SELECT * FROM main_carnumbers;")
results = cursor.fetchall()
print(results)

conn.close()
