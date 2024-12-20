from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Stelle sicher, dass der Ordner existiert, in dem die Dateien gespeichert werden sollen
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Prüfen, ob die Datei im Request vorhanden ist
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Wenn keine Datei ausgewählt ist
        if file.filename == '':
            return 'No selected file'
        if file:
            # Speichern der Datei
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'File successfully uploaded'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
