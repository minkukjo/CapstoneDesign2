import requests
import threading
import time

url = 'http://35.194.55.139'

def getrun():
	response = requests.get(url);
	if response.text != "Empty":
		print(response.text);
	threading.Timer(1.5,getrun).start()

getrun()
