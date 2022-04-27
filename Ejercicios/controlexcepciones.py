numero1 = 100
numero2 = 3
a="albacete"
try:
    print("otra instruccion 1")
    print("otra instruccion 2")
    print("otra instruccion 3")
    print(numero1/numero2)
    print("otra instruccion 5")
    c=int(a)
    print("otra instruccion 7")
    print("otra instruccion 8")
except ZeroDivisionError:
    print("Error, al dividir por cero") 
except ValueError:
    print("Error, Valor a convertir a numero desde texto erroneo")    
except:
    print('Error')
else:
    print("Las instrucciones se completaron en su totalidad")
finally:
    print('fin del programa')