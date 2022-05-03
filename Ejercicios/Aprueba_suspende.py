#Aprueba_suspende
#print("Ingrese calificacion 1")
Cal1=input("Ingrese calificacion 1:")
#print("Ingrese calificacion 2")
Cal2=input("Ingrese calificacion 2:")
#print("Ingrese calificacion 3")
Cal3=input("Ingrese calificacion 3:")

#if(Cal1.isdigit() and Cal2.isdigit() and Cal3.isdigit()):
try:
    #Validar la calificaciones
    Cal1=float(Cal1) #int(Cal1)
    Cal2=float(Cal2) #int(Cal2)
    Cal3=float(Cal3) #int(Cal3)
    if((Cal1>=0 and Cal1<=10) and (Cal2>=0 and Cal2<=10) and (Cal3>=0 and Cal3<=10)):
    #if( (Cal1 in range(0,11))  and (Cal2 in range(0,11)) and (Cal3 in range(0,11))  ):
        #Prom=(Cal1+Cal2+Cal3)//3
        Prom=(Cal1+Cal2+Cal3)/3
        if (Prom>=4):
            print("Aprueba")
        else:
            print("Suspende")
        #fin if
        print(Prom)
    else:
        print("El rango de las calificaciones no esta entre 0 y 10")
#else:
except:
    print("Por favor entre calificaciones con numericas")
#fin Aprueba_suspende
