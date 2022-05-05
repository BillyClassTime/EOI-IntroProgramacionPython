#Asignación simultanea

a=5
b=10
print("Paso 1. Valores iniciales")
print(a)
print(b)
c=b
b=a
a=c
del c
print("Paso 2. Valores intercambiados")
print(a)
print(b)

