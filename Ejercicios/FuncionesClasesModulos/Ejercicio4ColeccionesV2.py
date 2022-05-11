from random import randint

def avg(ciudades):
    averages = { ciudad: sum(grados)/len(grados) for ciudad,grados in ciudades.items() } #creates a dict with average of each subject
    #return averages | {"Promedio Ciudades": sum(vals:=averages.values())/len(vals) } #adds and returns the total average
    return averages 

ciudades=['Viena','Sofia','Berlín','Nicosia','Copenhague','Bratislava','Madrid','Bruselas','Paris','Oslo']
ciudade1=['Roma','Dublin','Londres','Lisboa','Budapest','Atenas','Reikiavik','Varsovia','Berna','Bucarest']
ciudades.extend(ciudade1)
# ciudad_temperatura={}
# for ciudad in ciudades:
#     ciudad_temperatura[ciudad]=[randint(-5,43) for i in range(1,13)]
ciudad_temperatura={ciudad:[randint(-5,43) for i in range(1,13)] for ciudad in ciudades}    # equivale a las lineas 11,12 y 13
#print(ciudad_temperatura)
#promedios = avg(ciudad_temperatura) | items() = Returns a list containing a tuple for each key value pair
ciudad_promedios = { ciudad: sum(grados)/len(grados) for ciudad,grados in ciudad_temperatura.items() }
#print(ciudad_promedios)
mas_alta = max(ciudad_promedios,key=ciudad_promedios.get)
mas_baja = min(ciudad_promedios,key=ciudad_promedios.get)
print("La ciudad con promedio anual de temperatura mas alta es:",mas_alta,"<->{:1.2f} ºC".format(ciudad_promedios[mas_alta]))
print("La ciudad con promedio anual de temperatura mas baja es:",mas_baja,"<->{:1.2f} ºC".format(ciudad_promedios[mas_baja]))
promedios_ordenados = sorted(ciudad_promedios,key=ciudad_promedios.get,reverse=True)
#print(promedios_ordenados)
for ciudad in promedios_ordenados:
    print(ciudad,",","{:1.2f} ºC".format(float(ciudad_promedios[ciudad])))