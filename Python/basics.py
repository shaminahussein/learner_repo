import requests as receivedData
r = receivedData.get('http://www.mindroom.edu.au')
print(r.text)