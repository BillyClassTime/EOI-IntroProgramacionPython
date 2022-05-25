import requests 

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {
        'offset': offset
    } if offset else {} #aca digo q is offset es q lo q nos pasan no sea 0 , sino mando dic vacio {}
    

    response = requests.get(url, params=args)

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results', [])

        if  results:
            for pokemon in results:
                name = pokemon['name']
                print(name)

        next = input("¿Continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)
    
if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'

    get_pokemons()