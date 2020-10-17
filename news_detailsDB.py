import sqlite3 as sql

con = sql.connect('news_data.db')
print("Database successfully open")

con.execute("CREATE TABLE news (url VARCHAR, title VARCHAR, news_text VARCHAR, label VARCHAR)")
print("Table created successfully")
con.close()