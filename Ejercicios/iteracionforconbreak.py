contadordenumerosenlaserie =0
for numero in range(1,21,2):
    contadordenumerosenlaserie+=1
    if (contadordenumerosenlaserie>=5):
        break # salte a la linea despues del bloque for
    print(numero)
    #print("otra instruccion 1")
    #print("otra instruccion 2")
    #print("otra instruccion 3")
    #print("otra instruccion 4") 
print("Numeros de la serie:",contadordenumerosenlaserie)