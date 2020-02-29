import sqlite3 

conn = sqlite3.connect("./main/db.sqlite3")
cursor = conn.cursor()

#cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
#conn.commit()

#cursor.execute("SELECT * FROM main_cards")
cursor.execute("INSERT INTO main_carnumbers VALUES (3,'one', 'two', 'three', 'four')")
conn.commit()
cursor.execute("SELECT * FROM main_carnumbers;")
results = cursor.fetchall()
print(results) 
cursor.execute("SELECT count(id) FROM main_carnumbers;")
results = cursor.fetchall()
print(results) 
conn.close()
