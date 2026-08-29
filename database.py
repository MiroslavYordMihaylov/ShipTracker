import sqlite3
import uuid
import auth

conn = sqlite3.connect('ship.db') 
cursor = conn.cursor()

command1 = """CREATE TABLE IF NOT EXISTS credentials (
        id UUID PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL)"""

cursor.execute(command1)

# Create a unique user id
user_id = str(uuid.uuid4())


def succ_registration():
    with conn:
        cursor.execute(
            "INSERT INTO credentials VALUES (?, ?, ?, ?)",
            (user_id, auth.username, auth.email, auth.password)
        )
    cursor.execute("SELECT * FROM credentials")

    result = cursor.fetchall()
    print(result)
    
    conn.close()