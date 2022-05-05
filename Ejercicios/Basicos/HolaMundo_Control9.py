# Hola mundo
#print("Hola mundo")

# Control Número 9

#N=0
print("Escribir el número")
N=input() #N="VALOR"
if(N.isdigit()):
    N=int(N)
    if (N==9):
        print("El número es igual a 9")
    else:
        if (N>9):
            print("El número es mayor a 9") 
        else:
            print("El número es menor a 9")
        #Fin Si
    #Fin Si
else:
    print("Por favor entre un valor númerico")
#Fin Control Número 9