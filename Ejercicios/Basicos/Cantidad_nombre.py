#Cantidad_nombre
#print("Ingresar Nombre")
while(True):
    nombre=input("Ingresar Nombre (N para finalizar):")
    if (nombre=="N"):
        print("Gracias por usar este programa")
        break
    #print("Ingresar Cantidad")
    Num=input("Ingresar Cantidad:")
    if (not nombre.isdigit()):
        if(Num.isdigit()):
            Num=int(Num)
            #print((f"{nombre}\n")*int(Num))  #reemplaza lineas 14,15 y 16
            while (Num>0):
                print(nombre)
                Num=Num - 1 
            #fin mientras
        else:
            print("Por favor entre la cantidad numérica")
    else:
        print("Por favor entre el nombre en texto")
    #finCantidad_nombre

