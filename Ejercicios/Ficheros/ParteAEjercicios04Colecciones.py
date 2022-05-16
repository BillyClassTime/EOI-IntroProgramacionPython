from random import randint
from ParteAEjercicio02Colecciones import lee_o_crea_fichero_apartir_de_una_coleccion as leer_escribir

ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}
for ciudad in ListaCiudades: # Recorremos la lista de ciudades
    listatemperaturas = [] # Creamos o "Reseteamos" la lista de temperaturas en cada recorrido del bucle, para que sean diferentes en cada ciudad.
    for i in range(0,12): 
        temperaturas = randint(0,50) # Generamos temperaturas comprendidas entre 0 y 50ºC
        listatemperaturas.append(temperaturas) #Almacenamos las temperaturas en una lista.
    dicc[ciudad] = listatemperaturas
print(dicc)

file='./Ejercicios/Ficheros/Data_ejercios04.txt'
leer_escribir(file,dicc)

