#SumaDigitos
nro=input("Ingrese un nro: ")
nro=int(nro)
resul=0
while(nro!=0):
    resul+= (nro%10)
    nro=nro//10
#fin while
print("El resultado es: " ,resul)
