import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Add users for fun
c.execute('CREATE TABLE users (id integer, username text, password text);')
c.execute('''INSERT INTO users VALUES (?,?,?)''', (1, 'admin', 'uYhQUkw=U}j}AX/N(FQJ ,k}?5!k^S\ Iy6'))

c.execute('CREATE TABLE messages (id INTEGER PRIMARY KEY, link text);')
c.execute('''INSERT INTO messages VALUES (?,?)''', (1, 'http://172.16.0.11'))

conn.commit()
conn.close()
