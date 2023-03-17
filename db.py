import sqlite3

conn = sqlite3.connect("players.db")
print("Opened Database successfully")

conn.execute("CREATE TABLE players (name TEXT, id INTEGER, score INTEGER)")
print("Table created successfully")
conn.close()