n=input("ingrese un número")
f=1
if (n.isdigit()):
    n=int(n)
    while n>1:
        f=f*n
        print(f"{n}  {f}")
        n=n-1
    print("el factorial es: ",f)
else:
    print("ingrese numero valido")