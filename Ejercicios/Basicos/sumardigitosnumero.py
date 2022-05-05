#Algoritmo SumaDigitos
nro = input("Ingrese un nro: ")
if (nro.isdigit()):
    nro = int(nro)
    resul = 0
    while nro != 0 : 
        resul = resul + (nro % 10)
        nro = nro//10
    #FinMientras
    print("El resultado es: ", resul)
else:
    print("Entre un número válido")
#FinAlgoritmo