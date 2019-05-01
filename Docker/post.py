import requests

url = 'http://35.194.55.139'
response = requests.post(url, {'word':'hey name is minkuk'})
print(response.text)
