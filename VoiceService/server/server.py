import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['m4a','txt','wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		
		#UPLOAD_FOLDER is not a configuration option recongnized by Flask
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
		print ('save success')
	return 'OK'
	

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
