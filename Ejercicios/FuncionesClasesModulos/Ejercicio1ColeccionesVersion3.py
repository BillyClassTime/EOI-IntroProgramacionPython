from random import randint
# En este programa, procesa las mujeres como 0 y los hombres como 1

lista = []

for i in range(0,100):

    lista.append(randint(0,1))



print(f"El porcentaje de mujeres es del: {lista.count(0)}%")

print(f"El porcentaje de hombres es del: {lista.count(1)}%")

if(lista.count(0) > lista.count(1)):

    print("Hay más mujeres que hombres")

elif(lista.count(0) == lista.count(1)):

    print("Hay igualdad")

else:

    print("Hay más hombres que mujeres")



respuesta = input("¿Quieres ver el total de los datos? ").lower()

if respuesta == 'si' or respuesta == 'sí' or respuesta == 's' or respuesta == 'yes' or respuesta == 'y':

    print("\nMujeres: {}".format(lista.count(0)))

    print("Hombres: {}".format(lista.count(1)))

    print("Lista: {}".format(lista))

    print("Total de personas: {}".format(len(lista)))