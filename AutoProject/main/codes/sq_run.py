import sqlite3 

conn = sqlite3.connect("TestDB.sqlite3")
cursor = conn.cursor()

cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
conn.commit()

cursor.execute("SELECT * FROM Artist ORDER BY Name LIMIT 3")
results = cursor.fetchall()
print(results) 

conn.close()
