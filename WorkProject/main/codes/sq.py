import sqlite3 

conn = sqlite3.connect("./../../db.sqlite3")
cursor = conn.cursor()

cursor.execute("INSERT INTO main_carnumbers VALUES \
        ((SELECT count(id) FROM main_carnumbers) + 1,\
        '{0}','{1}','{2}','{3}')".format('null', 'null', 'ffff','null'))
conn.commit()
    
    
conn.close()
