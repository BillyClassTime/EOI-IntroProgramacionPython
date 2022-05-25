from random import randint
from os.path import exists,split

def GestionFicherosValidacion(file_nombre,lista_datos):
    try:
        fichero=None
        carpeta, file = split(file_nombre)
        if (exists(carpeta)):
            if(exists(file_nombre)):
                fichero = open (file_nombre,'rt',encoding='UTF-8')
                contenido = fichero.read()
                print(f'Fichero:"{file}", previamente creado, este es su contenido:\n{contenido}')
            else:
                fichero = open(file_nombre,'wt',encoding='UTF-8')
                fichero.write(str(lista_datos))
                print(f'Fichero:"{file}" - generado')
        else:
            raise Exception(f"Carpeta:'{carpeta}' no existe")
        return True
    except Exception as e:
        print(f'E-1:{e}')
        return False
    finally:
        if fichero != None: fichero.close()

def connectBBDD(version=False):
    from pymongo import MongoClient


    clientDB = MongoClient('mongodb://localhost:27017/')
    db = clientDB.admin
    if(version):
        resultado = db.command('serverStatus')
        print('Host:',resultado['host'])
        print('Version:',resultado['version'])
        print('Process:',resultado['process'])
        print(clientDB.list_database_names())
    return clientDB

def CreateDB(name,clientDb):
    database_name=name # 'Estadisticas'
    db=clientDb[database_name]
    return db

#Create a collection
def createCollection(name,db):
    collection_name=name #'ListasTemperaturas
    collection=db[collection_name]
    #print(db.list_collection_names())
    return collection


#inserting documents in the collection
def insertDocument(document,col):
    id=randint(1,1000)
    docBB= {'Id':id,'Data':str(document)}
    col.insert_one(docBB)
    return id

#Retrieving the data from the collection
def retrievingDocument(query,col):
    result= col.find_one(query)
    return result['Data']


if __name__ == '__main__':
   # lista=["hola","caracola"] Aqui se pone el proceso de generar los datos
    lista=[]
   #
   # try:
    fichero_procesar='./datos/Data_ejercicios04.txt' #copiar aqui el fichero resultante de 
                                                     #almacenar los datos de las colecciones
    con=None
    db=None
    col=None
    if GestionFicherosValidacion(fichero_procesar,lista):
        print('Proceso inicia')
        fichero = open(fichero_procesar,'rt',encoding='UTF-8')
        contenido = fichero.read()
        con=connectBBDD();
        db=CreateDB('Estadisticas',con)
        col=createCollection('ListaTemperaturas',db)
        if (con!=None):
            id=insertDocument(contenido,col)
            query={'Id':id}
            res=retrievingDocument(query,col)
            lista=eval(res)
            print(lista)
    else:
        print('proceso no inicia')


    #except Exception as e:
        #print(f'E-0:{e}')
