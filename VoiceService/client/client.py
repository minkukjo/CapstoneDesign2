import sys
import requests

if not len(sys.argv) is 4:
    print ('argv #ip #port #fileName')
    sys.exit()

url = "http://"+sys.argv[1]+":"+sys.argv[2]+"/"
print(url)
#url = "http://13.125.167.133:5000/"
files = {'file':open(sys.argv[3],'rb')}

r = requests.post(url,files=files)
r.text

print(r)