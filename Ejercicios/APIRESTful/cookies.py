import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = {
        'my-cookie': 'true'
    } #para mandar cookies a traves de una peticion 
    response = requests.get(url, cookies=cookies)

    if response.status_code==200: 
        cookies = response.cookies
        print(cookies)

        print("El contenido es:")
        print(response.content)