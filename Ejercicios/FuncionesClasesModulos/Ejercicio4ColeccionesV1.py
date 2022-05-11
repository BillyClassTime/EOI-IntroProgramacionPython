#Hacer un programa que procese las temperaturas mensuales de 20 ciudades. Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y cual la más baja.
#También deberá sacar la lista de las 20 ciudades con el promedio de temperaturas anuales desde la más alta hasta la más baja.
from random import randint
ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']
dicc = {}
#{'Malaga':[0,1,2,3,4,5,6,7,8,9,10,11]}  #clave:la ciudad y valor la lista con las 12 temperaturas.
#{'Malaga':[0,1,2,3,4,5,6,7,8,9,10,11],'Alava':[0,1,2,3,4,5,6,7,8,9,10,11],..'Girona':[0,1,2,3,4,5,6,7,8,9,10,11]} #Asi se ve en la linea 15
for ciudad in ListaCiudades: # Recorremos la lista de ciudades
    listatemperaturas = [] # Creamos o "Reseteamos" la lista de temperaturas en cada recorrido del bucle, para que sean diferentes en cada ciudad.
    for i in range(0,12): 
        temperaturas = randint(0,50) # Generamos temperaturas comprendidas entre 0 y 50ºC
        listatemperaturas.append(temperaturas) #Almacenamos las temperaturas en una lista.
    dicc[ciudad] = listatemperaturas #Almacenamos en un diccionario el nombre de la ciudad junto a una lista con las temperaturas de enero a diciembre (12)
DiccPromedioAnual={} 
#{'Malaga':4,'Alava':3,...'Girona':23} Asi se ve enla linea 22
for clave,valor in dicc.items(): # Recorremos el diccionario
    print(f'{clave} -> {valor}') # Mostramos en pantalla los nombres de la ciudad junto a la lista de temperatura de todo el año
    tuplatemperaturas = tuple(valor) # Creamos una tupla con los valores del diccionario
    MediaAnuales = round(sum(tuplatemperaturas)/12 ,2) # Hacemos una media de las temperaturas anuales de cada ciudad
    DiccPromedioAnual[clave] = MediaAnuales # Creamos un nuevo diccionario con la ciudad y la temperatura media anual.
MaxProAnual = max(DiccPromedioAnual.values()) # Almacenamos el valor maximo del promedio anual
MinProAnual = min(DiccPromedioAnual.values()) # Almacenamos el vlaor minimo del promedio anual
#DiccPromedioAnual.keys()
#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom max anual.
print(f'\n La ciudad con el promedio anual mas ALTO 1 es { list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')
print(f'\n La ciudad con el promedio anual mas ALTO 2 es { max(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MaxProAnual} ºC')
#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom min anual.
print(f'\n La ciudad con el promedio anual mas BAJO 1 es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC \n') 
print(f'\n La ciudad con el promedio anual mas BAJO 2 es { min(DiccPromedioAnual,key=DiccPromedioAnual.get)} con un promedio de: {MinProAnual} ºC')
ListaPromedioAnual = list(DiccPromedioAnual.items()) #Convertimos el diccionario en una lista
ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True) # Ordenamos la lista de mayor a menor
print(f'La lista de las ciudades ordenadas es (1) :\n{ListaPromedioAnual}')
ListaPromedioAnual1 = sorted(DiccPromedioAnual,key=DiccPromedioAnual.get,reverse=True) #esta linea junto con las lineas 33 y 34
                                                                                       #equivalen a 28,29 y 30
for i in ListaPromedioAnual1:
    print(i,DiccPromedioAnual[i])