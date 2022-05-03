#3 - Paridad Numero
#print("ingrese un número")
nro=input("Ingrese un número:")
if (nro.isdigit()):
    nro=int(nro)
    if (nro%2==0):
        print("Es par")
    else:
        print("Es impar")
else:
    print("Por favor entre un número valido")