#fichero1 = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Mujeres).txt"
#fichero2 = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (Hombres).txt"
fichero1 = './Ejercicios/Ficheros/Data_chicas_ejercicio03.txt'
fichero2 = './Ejercicios/Ficheros/Data_chicos_ejercicio03.txt'

archivo1 = open(fichero1, "rt", encoding='UTF-8')
archivo2 = open(fichero2, "rt", encoding='UTF-8')

def devolver_lista(cadena):
    cadena = cadena.strip()
    cadena = cadena.strip('[')
    cadena = cadena.strip(']')
    return [int(x) for x in cadena.split(',')]

mujeres = devolver_lista(archivo1.read())
hombres = devolver_lista(archivo2.read())
archivo1.close()
archivo2.close()

mujeres.sort()
hombres.sort()

#fichero = "C:\\00-Python\\Ejercicios de Clase\\Ficheros\\Colecciones Ficheros II\\Datos_3 (B).txt"
fichero='./Ejercicios/Ficheros/Resultado_ejercicios03.txt'
archivo = open(fichero, "wt", encoding='UTF-8')

def calculo_lista(lista, genero):
    promedio = 0
    if genero == 'M':
        for i in lista:
            if i >= 18:
                archivo.write(f"Hay {len(lista[i:])} mujeres mayores de edad\n")
                break
        archivo.write(f"La mujer más joven tiene {min(lista)} años y la más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de las mujeres es de {} años\n".format(promedio/100))
    else:
        for i in lista:
            if i < 18:
                archivo.write(f"Hay {len(lista[i:])} hombres menores de edad\n")
                break
        archivo.write(f"El hombre más joven tiene {min(lista)} años y el más mayor {max(lista)} años\n")
        for i in lista:
            promedio += i
        archivo.write("El promedio de edad de los hombres es de {} años\n".format(promedio/100))


archivo.write("RESULTADOS DEL EJERCICIO 3:\n\n")
archivo.write("="*100+'\n')
archivo.write("Total de personas: {}\n".format(len(mujeres) + len(hombres)))
archivo.write("="*100+'\n')
sl='\n'
columna=1
archivo.write("\nMujeres:[")
for mujer in mujeres:
    #archivo.write("{}{}".format(mujer,('{}{}'.format(',',sl) if columna<=(len(mujeres)-1) else "]") if columna%30 == 0 else ','))
    archivo.write("{}{}".format(mujer,f'{","}{sl}' if columna%31 == 0 else (',' if columna<=(len(mujeres)-1) else "]")))
    columna+=1
print(columna)
archivo.write("\nHombres:[")
columna=1
for hombre in hombres:
    archivo.write("{}{}".format(hombre,f'{","}{sl}' if columna%31 == 0 else (',' if columna<=(len(hombres)-1) else "]")))
    columna+=1
archivo.write(f'{sl}{"="*100}{sl}')

calculo_lista(mujeres, 'M')
archivo.write("="*100+'\n')
calculo_lista(hombres, 'H')
archivo.write("="*100+'\n')
archivo.write(f"\nHay un total de {len(mujeres)} mujeres")
archivo.write(f"\nHay un total de {len(hombres)} hombres")