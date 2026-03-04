
from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            click_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()

        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
                  (original_url, short_code))
        conn.commit()
        conn.close()

        short_url = request.host_url + short_code

    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url, click_count FROM urls WHERE short_code=?",
              (short_code,))
    result = c.fetchone()

    if result:
        original_url, click_count = result
        c.execute("UPDATE urls SET click_count=? WHERE short_code=?",
                  (click_count + 1, short_code))
        conn.commit()
        conn.close()
        return redirect(original_url)
    else:
        conn.close()
        return "URL not found!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
