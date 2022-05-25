""""https://pokeapi.co/api/v2/pokemon-form?offset=20&limit=20","""
import requests
import json

def get_pokemons(url,offset=0):
    param={'offset':offset}
    r = requests.get(url,params=param)
    if r.status_code == 200 :
        resultado = r.json()
        lista_pokemons = resultado.get('results',[])

        if lista_pokemons:
            for pokemon in lista_pokemons:
                name = pokemon['name']
                print(name)
        continuar = input('Desdea seguir con mas pokemons?(Y/N)').lower()
        if continuar=='y':
            get_pokemons(url,offset+20)
    #print(r.text)

if __name__=='__main__':

    url = 'https://pokeapi.co/api/v2/pokemon-form'
    get_pokemons(url)

