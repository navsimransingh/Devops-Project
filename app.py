import os
import webbrowser
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            filepath = os.path.join('', photo.filename)
            photo.save(os.path.join('./files', photo.filename))
            query = "python python_files/virustotal.py {}".format(filepath)
            print(query)
            os.system(query)
    webbrowser.open_new_tab('http://localhost:8000')
    return redirect('localhost:8000')
    


if __name__ == '__main__':
    app.run()    