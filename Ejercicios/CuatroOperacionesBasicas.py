i=0             #Flag o bandera en castellano
while (i==0):
    try:
        e = float(input("¿Que operación realizo 0.Suma, 1.Resta, 2.Multiplicación o 3.División? Introducir número!!!"))
        x = float(input("¿Que valor asignamos a numéro 1? Introducir número!!!"))
        y = float(input("¿Que valor asignamos a numéro 2? Introducir número!!!"))
        #if x.replace(".","",1).isdigit() and y.replace(".","",1).isdigit():
        #x = float(x)
        #e = float(e)
        #y = float(y)
        if(e==0):
            z=x+y 
            print(f"El resultado de sumar {str(x)} y {str(y)} es: {str(z)}")
        elif(e==1):
            z=x-y
            print(f"El resultado de restar  {str(x)} y {str(y)} es: {str(z)}")
        elif(e==2):
            z=x*y
            print(f"El resultado de multiplicar {str(x)} por {str(y)} es: {str(z)}")
        elif(e==3):
            if(y==0):
                print(f"el valor de num2 no puede ser {y}")
            else:
                z=x/y
                print(f"El resultado de dividir {str(x)} entre {str(y)} es: {str(z)}")
        else:
            print("Número introducido no corresponde con ninguna operación")   
        #else:
    except:
            print('entre valores numericos válidos')

    e = 3
    while (e!=0 and e!=1):
        e=input("Desea seguir realizando operaciones 1.Si 0.No:")
        if e.isdigit() :
            e=int(e)
            if (e==1):
                i=0
            elif(e==0):
                i=1
            else:
                print("Valor introducido erroneo")
        else:
            print('entrada invalida')