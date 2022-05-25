import requests
import json
url='http://httpbin.org/post' #endpoint de conexión 
     #http://httpbin.org/post
user = json.dumps({'Username':'Billy'})
header = {'content-type':'application/json'}
r = requests.post(url,data=user,headers=header)
print(r.text)