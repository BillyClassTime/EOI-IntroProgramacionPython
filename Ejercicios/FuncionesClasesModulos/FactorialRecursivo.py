def Factorial(N):
    if N<=0:
        #Esto queda pendiente ...
        #generar una excepcion
        raise 
        #pass

    if (N<=1):
        print('return 1')
        return 1
    else:
        print('return {} Factorial({}-1)'.format(N,N))
        return N * Factorial(N-1)

n=input("Desea calcular el factorial de (Entre un numero):")
try:
    n=int(n)
    r=Factorial(n)
    print("El factorial de:",n," es ",r)
except TypeError:
    print('Entre un número válido')
except ValueError:
    print('Entre un número válido')
except:
    print('No se permiten valores menores a 0')
