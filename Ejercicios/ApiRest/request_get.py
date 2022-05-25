import requests
r = requests.get('http://api.open-notify.org/iss-now.json')
print(r.text)
print('Longitud de la ISS:',r.json()['iss_position']['longitude'])
print('Latitud de la ISS:',r.json()['iss_position']['latitude'])