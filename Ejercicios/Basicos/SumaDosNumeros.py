Num1=input("Escribir el numero 1:")
Num2=input("Escribir el numero 2:")
if (Num1.isdigit() and Num2.isdigit()):
    Num1=int(Num1)
    Num2=int(Num2)
    Rta=Num1+Num2
    print(f"El resultado es:{Rta}")
    #print(f"El resultado es:{int(Num1)+int(Num2)}")
else:
    print("Los valores entrados no son números validos")