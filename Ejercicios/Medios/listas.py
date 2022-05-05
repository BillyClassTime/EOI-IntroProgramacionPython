colores=["Red","Yellow","Green"]
print(colores[1])
colores.append('Black')
colores.insert(2,'Orange')
print('Lista de colores:',colores)
try:
    color=input('Entre el color para saber su poicion:')
    print("Posicion del color en la lista ",colores.index(color))
except ValueError:
    print('el color no esta en lista')

colores.remove('Yellow') #Error de ValueError si el elemento
                         #no esta en la lista

print('Lista de colores actualizada:',colores)

print('Color en la posicion 2:',colores[2])

colores_alternativos=['Magenta','Blue','Pink']
colores.extend(colores_alternativos)
print('Lista de colores actualizada despues del extend:',colores)

colores.pop(2)  #Borrará 
print('Lista de colores actualizada despues del pop:',colores)

colores.sort()
print('Lista de colores actualizada despues del sort:',colores)

print(colores*2)