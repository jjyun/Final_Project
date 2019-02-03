import os
from flask import Flask, request, jsonify, render_template


import os
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)
    if request.files.get('file'):
        file = request.files['file']
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    return render_template('index.html')   

if __name__ == "__main__":
    app.run(debug=True)