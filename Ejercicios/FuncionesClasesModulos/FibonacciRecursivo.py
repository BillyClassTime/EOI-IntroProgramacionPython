def Fivonacci(N):

    if(N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return Fivonacci (N-1) + Fivonacci (N-2)

n=input("Introduce la posicion de fivonnaci: ")
try:
    n=int(n)
    serie_fibonacci=[]
    for i in range(1,n+1):
        r=Fivonacci(n)
        serie_fibonacci.append(r)
    print(f"el numero en esa posición es {r}")
    print('La serie es:',*serie_fibonacci)
    #a,b,c = *serie_fibonacci
except ValueError:
    print("Numero invalido")
except TypeError:
    print("Numero no valido")
except:
    print("faio")
