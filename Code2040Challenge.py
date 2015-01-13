import requests
url = "http://challenge.code2040.org/api/register"
data = {'email': 'nzoner12@yahoo.com', 'github':'https://github.com/ComicStix'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
