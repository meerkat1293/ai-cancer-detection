import os
#import magic
import urllib
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from sample_func import sample_func

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			if sample_func(file.filename[-4:]):
				flash('This is a text file')
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
			filename = 'http://127.0.0.1:8887/' + file.filename
			return render_template('upload.html', filename=filename)
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif, csv')
			return redirect(request.url)




if __name__ == "__main__":
    app.run()