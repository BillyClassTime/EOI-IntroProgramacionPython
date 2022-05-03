#Suma de Pares 
suma = 0
nro = 2
while (nro<=1000000):
    #if(nro%2 == 0):
        #suma=suma+nro
    suma+=nro
    #fin si
    #nro=nro+1
    nro+=2
#fin while
print(f"la suma de los pares entre 2 y 1000000 es {suma}")