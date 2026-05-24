from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS test (
    id SERIAL PRIMARY KEY,
    message TEXT
)
""")
conn.commit()

@app.route("/")
def home():
    return "Serveur + base OK 🚀"

@app.route("/add")
def add():
    cur.execute("INSERT INTO test (message) VALUES ('Bonjour')")
    conn.commit()
    return "Ajouté ✅"

@app.route("/data")
def data():
    cur.execute("SELECT * FROM test")
    return str(cur.fetchall())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
