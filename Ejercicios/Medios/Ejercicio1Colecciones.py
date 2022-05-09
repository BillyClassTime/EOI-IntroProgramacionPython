#Ejercicio1.py
from random import randint
from Ejercicios1_Con_ClasificaGenero import ClasificaGenero

personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 para chicas y el 1 los chicos
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
print(personas)

ClasificaGenero(personas)

#Version sin llamar  a la funcion "ClasificaGenero"
"""
no_chicos= personas.count("M")
no_chicas= personas.count("F")


if no_chicos == no_chicas:
    print("Hay igualdad entre chicos y chicas")
elif no_chicos >no_chicas:
    print("hay mas chicos que chicas")
else:
    print("hay mas chicas que chicos")

print('El porcentaje de chicos es:{0}% y el de chicas:{1}%'.format(no_chicos,no_chicas))
"""

