import requests
#r=requests.get('http://api.open-notify.org/iss-now.json')
r=requests.get('https://httpbin.org/get')
print(type(r))
print(r.headers)
print(r.headers['content-type'])
print(f'{r.status_code}/{r.encoding}')
print(r.text)
#print(r.json()['message'])
print('JSON:',r.json())




