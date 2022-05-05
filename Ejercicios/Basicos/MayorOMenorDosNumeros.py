x=int(6)            #Numero dado

print("Introducir un número ")
y=input()
if (y.isdigit()):
    y=int(y)
    if(x>=y):
        print(f"{x} mayor ")
        
    else:
        print(f"{y} mayor ")
else:
    print('Entre un número valido')