from random import randint
import sys
sys.path.append('.\Ejercicios\Ficheros')
from ParteAEjercicio02Colecciones import lee_o_crea_fichero_apartir_de_una_coleccion as leer_escribir
print(f'Ejecicion 03:{__name__}')
#if __name__ == '__main__':
mujeres=[]
hombres=[]
# for n in range(1,101):
#     genero=randint(0,1)
#     if (genero==1):
#         mujeres.append(randint(0,101))
#     else:
#         hombres.append(randint(0,101))
#Las siguientes 3 lineas son equivalentes a las lineas 10,11,12,13,14 y 15
genero = [randint(0,1) for n in range(1,101)]
mujeres = [randint(0,101) for g in genero if g==1]
hombres = [randint(0,101) for g in genero if g==0]
fileChicos='./Ejercicios/Ficheros/Data_chicos_ejercicio03.txt'
fileChicas='./Ejercicios/Ficheros/Data_chicas_ejercicio03.txt'
#ParteAEjercicio02Colecciones.lee_o_crea_fichero_apartir_de_una_coleccion(fileChicas,mujeres)
#ParteAEjercicio02Colecciones.lee_o_crea_fichero_apartir_de_una_coleccion(fileChicos,hombres)
leer_escribir(fileChicas,mujeres)  #Equivale a la linea 20 si la linea 2 esta sin comentario y la 3 esta con comentario
leer_escribir(fileChicos,hombres)  #Equivale a la linea 21 si la linea 2 esta sin comentario y la 3 esta con comentario
