#Divisores_de_numero
while(True):
    print("Ingrese Numero entero,(N para salir):")
    Num=input()
    if (Num.isdigit()):
        #Num=int(Num)
        Num=float(Num)
        div=1
        while (div<=Num):
            if (Num%div == 0):
                print(div)
            #Fin Si
            #div=div+1
            div+=1
        #Fin While
    else:
        if (Num=="N"):
            break
        print("Por favor entre un número valido")
    
#Fin Divisores_de_numero

