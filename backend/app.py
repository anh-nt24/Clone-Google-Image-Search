from flask import Flask
from flask import render_template, jsonify
from flask import redirect, url_for
import os, sys
from flask import flash, request, send_from_directory
from werkzeug.utils import secure_filename
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.cbir import cbir

UPLOAD_FOLDER = 'static/storage/upload'
allowed_extensions = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.split('.')[1].lower() in allowed_extensions

@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html', title='Searching Page')
    list_img = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.system(f'rm -rf {UPLOAD_FOLDER}/*')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            list_img = processing(filename)
    if list_img is not None:
        return jsonify({'htmlresponse': 
                render_template('response.html', title='Searching Page', list_img = list_img, len = len(list_img[1]))})

def processing(name):
    send_from_directory(app.config["UPLOAD_FOLDER"], name)
    path = f'../backend/{UPLOAD_FOLDER}/{name}'
    origin, res = cbir(path)
    origin = origin.split('/')[-1]
    st = ' '.join(res)
    os.system(f'cp -f {st} {UPLOAD_FOLDER}')
    st = st.replace('../images/', '')
    result = st.split(' ')
    return [origin, result]

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='storage/upload/' + filename))

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/')
def root():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)