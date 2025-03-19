from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (Replace this with a database later)
notes_list = []

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note = request.form.get("note")
        if note: 
            notes_list.append(note)  # Store note
        return redirect(url_for('notes'))  # Redirect back to /notes
    
    return render_template('index.html', notes=notes_list)  # Always send notes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
