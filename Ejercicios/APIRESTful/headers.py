import requests
import json
url='http://httpbin.org/post'
user = json.dumps({'Username':'Billy'})
headers={'content-type':'application/json'}
r = requests.post(url,data=user,headers=headers)
print(r.text)