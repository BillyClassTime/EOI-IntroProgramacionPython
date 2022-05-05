#tresnumeros
#print("Ingrese numero 1")
Num1=input("Ingrese numero 1:")
#print("Ingrese numero 2")
Num2=input("Ingrese numero 2:")
#print("Ingrese numero 3")
Num3=input("Ingrese numero 3:")
try:
    Num1=float(Num1)
    Num2=float(Num2)
    Num3=float(Num3)
    if(Num1<0):
        Resul=Num1 * Num2 * Num3
    else:
        Resul=Num1 + Num2 + Num3
    #fin si
    print(Resul)  
except ValueError:
    print("Por favor los números deben ser numéricos")
except:
    print("Error")
#fin tresnumeros  