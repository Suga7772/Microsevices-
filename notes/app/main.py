from flask import Flask, render_template, request, redirect
import sqlite3, os

app = Flask(__name__, template_folder=os.path.abspath('../templates'))
# Create database
def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/note', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            conn = sqlite3.connect('notes.db')
            c = conn.cursor()
            c.execute("INSERT INTO notes (content) VALUES (?)", (note,))
            conn.commit()
            conn.close()
            return redirect('/')

    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = c.fetchall()
    conn.close()
    
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3007, debug=True)
