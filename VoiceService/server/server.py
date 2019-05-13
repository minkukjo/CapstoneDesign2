import os
from flask import Flask, flash, request, redirect, url_for,Response,json
from werkzeug.utils import secure_filename

#TARGET_HOST = ''
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['m4a','txt','wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['GET','POST'])
def upload_file():
	print ("upload_file")
	if request.method == 'POST':
		file = request.files['file']
		
		#UPLOAD_FOLDER is not a configuration option recongnized by Flask
		print (os.path.join(app.config['UPLOAD_FOLDER']))
		#print (secure_filename(file.file_name))
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
		
		#Replace ':' to "" for file name
		wavFileName = file.filename
		wavFileName = wavFileName.replace(":","")
		print (wavFileName+' save success')

		encodeText = run_quickstart(wavFileName)
		# data = {
		# 	'msg' : encodeText
		# }
		# js = json.dumps(data)
		# resp = Response(js,status=200,mimetype='application/json')
		# return resp
		#print("encodeText : "+encodeText)

		f = open("result.txt", 'a')
		f.write(str(encodeText))
		f.close()
		#else
			
	return 'OK'
	
	
def run_quickstart(wavFileName):
	import io

	from google.cloud import speech
	from google.cloud.speech import enums
	from google.cloud.speech import types
	# [END speech_python_migration_imports]
	print ('run_quickstart'+wavFileName)
	
	# Instantiates a client
	# [START speech_python_migration_client]
	client = speech.SpeechClient()

	# [END speech_python_migration_client]

	# The name of the audio file to transcribe
	file_name = os.path.join(os.path.dirname(__file__),'uploads/',wavFileName)

	print ("file_name = "+file_name)

	# Loads the audio into memory
	with io.open(file_name, 'rb') as audio_file:
		content = audio_file.read()
		audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
		sample_rate_hertz=16000,
		language_code='ko-KR')

	# Detects speech in the audio file
	response = client.recognize(config, audio)

	for result in response.results:
		#result = request.post(TARGET_HOST, {'word': result.alternatives[0].transcript})
		print('Transcript: {}'.format(result.alternatives[0].transcript))
		return format(result.alternatives[0].transcript)

	# [END speech_quickstart]

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
