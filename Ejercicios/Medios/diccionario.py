dicColores={"red":"rojo","blue":"azul","green":"verde"}
print("Diccionario inicial:",dicColores)
dicColores["black"]="negro"     #Añadir un elmento al diccionario dado su clave/valor
print("Diccionario despues de añadir el color negro:",dicColores)
dicColores.pop("green")         #Quitar un elemento del diccionario dado su clave
print("Diccionario despues de quitar el color verde:",dicColores)

print("Red en castellano:",dicColores["red"])
print("Blue en castellado:",dicColores["blue"])

for key in dicColores:
    print(key,'->',dicColores[key])
