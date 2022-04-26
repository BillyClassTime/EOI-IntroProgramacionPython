ciudad="madrid"
print(ciudad.isdigit())
minombre="billy miguel"
print(len(minombre))

print(minombre[0])
print(minombre[1])
print(minombre[4])
#print(minombre[5]) Error out of index
print(minombre[2:])
print(minombre[:3])
print(minombre[2:4])
print("2:"+minombre[2])
print("-2"+minombre[-2])
print(minombre[1:10])
print(minombre[-4])

mensaje = "dd"
ciudad = "albacete"
print("hola {m} de {c}".format(m=mensaje,c=ciudad))
#print("hola "+mensaje+" de "+ciudad)
#print("hola "+mensaje) No es una forma eficiente de concatenar cadenas de caracteres

numero = 10/3
print("El número sin formato es:{}".format(numero))

print("El número con formato es:{n:1.2f}".format(n=numero))

print(f"Hola {mensaje} de {ciudad}")