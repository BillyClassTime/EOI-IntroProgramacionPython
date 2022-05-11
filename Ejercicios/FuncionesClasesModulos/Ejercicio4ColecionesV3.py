from random import randint
import operator

NombreCiudades={"Madrid","Barcelona","Sevilla","Malaga","Cordoba","Toledo","Valencia","Bilbau","Salamanca","Palma","Caceres","Segovia","Saragoça ","Cuenca","Alicante","Las Palmas","Avila","Merida","Granada","Murcia"}
ciudades= dict()

for i in NombreCiudades:
    media_temperaturas=0 
    for j in range (0,12):
        media_temperaturas+=randint(-10,40)
    ciudades[i]=media_temperaturas//12

#items()-Devuelve una lista de tuplas,  el primero será la clave y el segundo, su valor.
#key- Una funcion que sirve como llave para la comparacion de classificacion
ciudades_sort = sorted(ciudades.items(), key=operator.itemgetter(1),reverse=True)

mayor_media=ciudades_sort[0][0]
menor_media=ciudades_sort[len(ciudades_sort)-1][0]

print("La(s) ciudad(es) con mayor media anual es(son):")
for i in range (1,20):
    print(f"{mayor_media} con: {ciudades[mayor_media]}° grados")
    if(ciudades_sort[i][1]==ciudades[mayor_media]):
        mayor_media=ciudades_sort[i][0]
    else:
        break

print("\nLa(s) ciudad(es) con menor media anual es(son):")
for i in range (18,0,-1):
    print(f"{menor_media} con: {ciudades[menor_media]}° grados")
    if(ciudades_sort[i][1]==ciudades[menor_media]):
        menor_media=ciudades_sort[i][0]
    else:
        break

print("\nCiudades: ")
for i in range (0,20):
    print(f"{ciudades_sort[i][0]} = {ciudades_sort[i][1]}°")