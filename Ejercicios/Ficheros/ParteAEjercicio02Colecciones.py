from random import randint
from os.path import exists

def lee_o_crea_fichero_apartir_de_una_coleccion(file_nombre,lista_datos):
    try:
        if(exists(file_nombre)):
            fichero = open (file_nombre,'rt',encoding='UTF-8')
            contenido = fichero.read()
            print(f'Fichero previamente creado, este es su contenido:\n{contenido}')
        else:
            fichero = open(file_nombre,'wt',encoding='UTF-8')
            fichero.write(str(lista_datos))
            print(f'Fichero:{file_nombre} - generado')
    except Exception as e:
        print(f'E:{e}')
    finally:
        fichero.close()

print(f'Ejecicion 02:{__name__}')
if __name__ == '__main__':   
    personas=[]
    for n in range(1,101):
        personas.append(randint(0,125))
    personas1 = [randint(0,125) for i in range(1,101)] # equivale a las lineas 3, 4 y 5

    file  = './Ejercicios/Ficheros/Datos_ejercio02.txt'
    file1 = './Ejercicios/Ficheros/Datos_ejercio02A.txt'

    lee_o_crea_fichero_apartir_de_una_coleccion(file,personas)
    lee_o_crea_fichero_apartir_de_una_coleccion(file1,personas1)
else:
    pass