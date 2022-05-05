#MAYOR DE 3  
print("Ingrese numero 1")
Num1=input()
print("Ingrese numero 2")
Num2=input()
print("Ingrese numero 3")
Num3=input()
#if(Num1.isdigit() and Num2.isdigit() and Num3.isdigit()):
if(Num1.replace(".","",1).isdigit() and  Num2.replace(".","",1).isdigit() and Num3.replace(".","",1).isdigit()):
    Num1=float(Num1) #int(Num1)
    Num2=float(Num2) #int(Num2)
    Num3=float(Num3) #int(Num3)
    if(Num1>Num2 and Num1>Num3):
        Resul=Num1
        print("Numero mayor es : " ,Resul)
    else:
        if(Num2>Num1 and Num2>Num3):
            Resul=Num2
            print("Numero mayor es : " ,Resul)
        else:
            if (Num3>Num2 and Num3>Num1):   
                Resul=Num3
                print("Numero mayor es : " ,Resul)
            else:
                if (Num1==Num2):
                    Resul=Num1 #Num2
                else:
                    Resul=Num3
                print("Numero mayor es : " ,Resul) 
                #print("Hay numeros iguales") 
else:
    print("Introduzca un numero valido")       