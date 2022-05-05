colores=["Red","Yellow","Green"]
colores_alternativos=['Magenta','Blue','Pink']
colores.extend(colores_alternativos)
colores.sort() #Orden ascendente
print('Lista de colores actualizada despues del sort:',colores)

colores.sort(reverse=True)
print('Lista de colores actualizada despues del sort descendente:',colores)
