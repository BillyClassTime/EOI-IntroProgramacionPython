# %%
#Comentarios
text = """Escribamos valores alfanumericos 
       en distintas lineas. """

# %%
#Asignación simultanea
a=5
b=10
print("Paso1. Valores iniciales")
print(a)
print(b)

# %%
a=5
b="25"
c="25.7"
print("Número:" + str(a))
print(int(b))
print(float(c))

# %%
cadena="Hola mundo"
print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:2])
print(cadena[2:6])
print(cadena[-2])
print(len(cadena))

# %%
mensaje = "Mundo"
print ("Hola "+mensaje + " !!!")
print ("Hola {}!!!".format(mensaje))
print ("Hola {s} !!!".format(s=mensaje))
print (f"Hola {mensaje}!!!")
numero = 10/3
print (numero)
print ("Hola{n:1.2f}!!!".format(n=numero))

# %%
from datetime import datetime
datenow1 = datetime.now().date()
#print(f"Hora:{datenow1.hour}:{datenow1.minute}")
print("Fecha:",datenow1)
datenow2 = datetime.now()
print("Fecha:",datenow2)
print("Año:",datenow2.year)
print("Mes:",datenow2.month)
print("Dia:",datenow2.day)
print(f"Hora:{datenow2.hour}:{datenow2.minute}")

# %%
from datetime import datetime
fecha = "10-11-2022"
obj = datetime.strptime(fecha,'%m-%d-%Y')
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")

# %%
from datetime import datetime
fecha = datetime.now()
print(fecha.strftime("%A %d %b %Y"))

# %% [markdown]
# 

# %%
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dt =datetime.strptime('29/04/2022','%d/%m/%Y') #datetime.now()

print(dt)
print('\nDirectívas\n-------------------------------')
print('Día de semana corto       ' + dt.strftime(': %a'))
print('Día de la semana largo    ' + dt.strftime(': %A'))
print('Número de dia de la semana' + dt.strftime(': %w'))
print('Día del mes               ' + dt.strftime(': %d'))
print('Nombre del mes corto      ' + dt.strftime(': %b'))
print('Nombre del mes largo      ' + dt.strftime(': %B'))
print('Numero del mes            ' + dt.strftime(': %m'))
print('Año version corta         ' + dt.strftime(': %y'))
print('Anyo version larga        ' + dt.strftime(': %Y'))
print('Hora formato (00-23)      ' + dt.strftime(': %H'))
print('Hora formato (00-11)      ' + dt.strftime(': %I'))
print('AM/PM                     ' + dt.strftime(': %p'))
print('Minutos                   ' + dt.strftime(': %M'))
print('Segundos                  ' + dt.strftime(': %%'))

print('\nFormato de texto de fechas\n--------------')
print(dt.strftime('%a %d-%m-%Y'))
print(dt.strftime('%a %d/%m/%Y'))
print(dt.strftime('%a %d/%m/%y'))
print(dt.strftime('%A %d-%m-%Y, %H:%M:%S'))
print(dt.strftime('%X %x'))

# %% [markdown]
# 

# %%
import time
print("Time:",time.time())
print(time.localtime(time.time()))
print("Año:",time.localtime(time.time()).tm_year)
print("Minutos:",time.localtime(time.time()).tm_min)
print("Milisegundos:",int(time.time()*1000.0))
print(time.asctime(time.localtime(time.time())))

# %%
from datetime import datetime
from datetime import timezone
import pytz

print (pytz.all_timezones)
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))


# %%
a = 10
b = 20
if (a>b):
    print (f"el número mayor es {a}")
else:
    if (b>a):
        print(f"El número mayor es {b}")
    else:
        print ("los dos números son iguales")

# %%
lenguajes = ['python','c','c++','java']
for lenguaje in lenguajes:
    print(lenguaje)
for numero in range(3):
    print(numero)
for numero in range(len(lenguajes)):
    print(f"P:{numero} - V:{lenguajes[numero]}")

# %%
a = 10
b = 20
if (a>b):
    print (f"el número mayor es {a}")
elif (b>a):
    print(f"El número mayor es {b}")
else:
    print ("los dos números son iguales")

# %%
print("Instrucción antes del while")
valor = 0
while(valor < 5):
    valor += 1
    if (valor == 3):
        continue
    print(f"Valor actual:{valor}") 
print("Instrucción después del while")

# %%
numero1 = 100
numero2 = 0

try:
    print(numero1/numero2)
except ZeroDivisionError:
    print("Error al dividir por cero.")
except:
    print("Error")
else:
    print("La división se calculo correctamente.")
finally:
    print("Fin del programa")

# %% [markdown]
# Colecciones y JSON

# %%
colores=["Red","Yellow","Green"]
colores.append("Black")
colores.insert(2,"Orange")
print("Lista de colores:",colores)

print("Posicion color Yellow:",colores.index("Yellow"))
colores.remove("Yellow") #Remueve la primera 

print("Color en la posición 2:",colores[2])
print("Lista de colores:",colores)

# %%
colores1=["Red Strong","Yellow Dark","Ligth Green"]
colores2=["Magenta","Pink","Blue"]
print(colores2)
colores2.extend(colores1)
print(colores2)
colores2.pop(2)
print(colores2)


# %%
numeros = (17,89,21,988,42,429,32,834)
print(numeros[4])
print(list(enumerate(numeros)))
print(max(numeros))
print(min(numeros))
print(sum(numeros))

# %%
ciudades = {"madrid","albacete","sevilla"}
ciudades.add("valencia")
print("Conjunto de ciudades:",ciudades)
ciudades.discard("albacete")
print("Conjunto de ciuades:",ciudades)
for ciudad in ciudades:
    print(ciudad)
print(len(ciudades))

# %%
dicc= {"red":"rojo", "blue":"blue", "green":"verde"}
dicc["black"]="negro"
print(dicc)
dicc.pop("blue")
print(dicc)
print(dicc["red"])
for key in dicc:
    print(key,'->',dicc[key])

# %%
dicc= {"red":"rojo", "blue":"blue", "green":"verde"}
print(dicc.get("red","no exite"))

# %%
import json
citricos = ["limon","naranja","pomelo","lima"]
citricosJSON=json.dumps(citricos)
print("Json de citricos:",citricosJSON)
print(citricos)

# %% [markdown]
# Ejercicios iniciales de Python

# %%
print('hola mundo')

# %%
#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('Escribir el número')
n = input()
if (int(n)==9):
    print('El número es igual a 9')
else:
    if (int(n)>9):
        print('el número es mayor a 9')
    else:
        print('el número es menor a 9')


