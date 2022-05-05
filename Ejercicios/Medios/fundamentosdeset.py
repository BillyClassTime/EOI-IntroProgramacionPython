ciudades={'Madrid','Albacete','Vigo','Palencia','Sevilla','Sevilla','Vigo'}
print(ciudades)
ciudades.add('Valencia')
ciudades.add('Gijon')
print(ciudades)
for ciudad in ciudades:
    print(ciudad)
ciudades.discard('Palencia')
print('Conjunto (set) de Ciudades después de borrar a Palencia')
for ciudad in ciudades:
    print(ciudad)
