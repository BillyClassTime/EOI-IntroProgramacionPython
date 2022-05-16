from os.path import exists
# def fichero_existe(file):
#     try:
#         open(file)
#     except FileNotFoundError:
#         return False
#     return True

try:
    file='./Ejercicios/Ficheros/file_300.csv'
    #fichero_existe=False
    #if(fichero_existe(file)):
    if(exists(file)):
        fichero=open(file,'rt',encoding='UTF-8')
        contenido=fichero.read()
        if (len(contenido)>0):
            print(contenido)
        else:
            print('El fichero no tiene contenido')
    else:
        fichero=open(file,'wt',encoding='UTF-8')
        contenido = f'{file},árbol,limón,mandarina,naranja'
        fichero.write(contenido)
        print('escrito el contenido')
except Exception as e:
    print (f'E:{e}')
finally:
    fichero.close()

