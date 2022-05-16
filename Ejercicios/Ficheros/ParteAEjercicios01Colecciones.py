from random import randint
from os.path import exists
import sys
sys.path.append('.\Ejercicios\FuncionesClasesModulos')
#import Ejercicios1_Con_ClasificaGenero
from Ejercicios1_Con_ClasificaGenero import ClasificaGenero as Clasi
personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 para chicas y el 1 los chicos
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
print(f'Lista de personas:\n{personas}')

Clasi(personas)

try:
    file='./Ejercicios/Ficheros/Datos_ejercicios01.txt'
    if (exists(file)):
        print('Fichero previamente generado no se sobrescribe')
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        print(f'El contenido del fichero es:\n{contenido}')
    else:
        fichero=open(file,"wt",encoding='UTF-8')
        #fichero.write(personas) #E:write() argument must be str, not list
        fichero.write(str(personas))
except Exception as e:
    print(f'E:{e}')
finally:
    fichero.close()

