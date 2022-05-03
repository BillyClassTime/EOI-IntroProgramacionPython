#NumerosPrimos
numerodePrimos = input("Número de primos a mostrar:")
if (numerodePrimos.isdigit()):
    numerodePrimos=int(numerodePrimos)   #Convertir la entrada de tipo TEXTO "3"  a numero 3
    #iteracion
    #for nro in range(1,numerodePrimos+1):# numerodePrimos = 1 hasta numerosdePrimos<(nro+1) y paso 1
                                          # For no es util aqui porque no mostraría los N números primos
    nro=1                                 # nro es para el while el for lo inicia automáticamente  
    while numerodePrimos >0  :            # Contador =1  hasta que Contador == numerosDePrimos cada primo suma Contador HAGA
        div = 2                           # Mientras que numerosDePrimos > 0 (cada primo restaNumeroDePrimos) 
        band = True    #Boolean para comprobar si el numero es primo o no
        if nro==1 :    
                print(f"{nro} es primo")
                numerodePrimos-=1
        else: 		             
            while band and (nro>div) :   #band==True equivalente band
                if (nro % div) == 0 :
                    band = False
                    break
                #FinSi
                div += 1 #div = div +1
            #FinMientras
            if band :                    #band==True equivalente band
                print(f"{nro} es primo")
                numerodePrimos-=1
            #else:
            #    print("No es primo")
            #FinSi
        #FinSi
        nro+=1
else:
    print('Por favor entre un número valido')