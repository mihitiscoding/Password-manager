import sqlite3

conn = sqlite3.connect('locking_data.db')

guide = conn.cursor()

guide.execute("SELECT * FROM entry")

index_refer = guide.fetchall()

for index in index_refer:
    print(f" | {index[0]} | {index[1]} | {index[2]}|\n")

conn.commit()


conn.close()

