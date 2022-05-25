import requests
url='http://www.python.org/images/success/nasa.jpg'

r = requests.get(url,stream=True)

with open('./data/imagen_downloade.jpg','wb') as file:
    for trozo in r.iter_content():
        file.write(trozo)

r.close()