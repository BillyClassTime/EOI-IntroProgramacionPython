Num1=input("Ingrese un numero(1): ")
Num2=input("Ingrese un numero(2): ")
Num3=input("Ingrese un numero(3): ")
try:
    Num1=float(Num1)
    Num2=float(Num2)
    Num3=float(Num3)
    if(Num1>=Num2 and Num1>=Num3):
        result=Num1
    if(Num2>=Num1 and Num2>=Num3):
        result=Num2
    if(Num3>=Num1 and Num3>=Num2):
        result=Num3
    print("El numero mayor es :",result)
except ValueError:
    print("Por favor intruduzca un numero en cada casilla")