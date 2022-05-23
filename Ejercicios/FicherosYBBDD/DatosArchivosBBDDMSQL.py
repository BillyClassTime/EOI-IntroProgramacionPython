from itertools import count
from multiprocessing import connection
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
    #Create a Database Estadisticas 
    import pyodbc
    """
    CREATE TABLE DatosEstadisticos(
	id int IDENTITY(1,1) NOT NULL,
	contenidoEstadistico nvarchar(2224) NULL)
    """    
    server = '(localdb)\ProjectsV13'
    database = 'Estadisticas' 
    username = 'developer' 
    password = 'P4$$w0rd' 

    #Conecction String
    driver='DRIVER={ODBC Driver 17 for SQL Server};'
    others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection_string='{}{}'.format(driver,others)
    con = pyodbc.connect(connection_string)
    #with pyodbc.connect(connection_string) as cur:
    with con as wcon:
        res=wcon.cursor().execute("SELECT @@VERSION AS 'SQL Server Version Details'")
        if (version):
            for r in res:
                print(r[0])
    return con

def insertarDatosEstadisticosBBDD(con,contenido):
    with con as wcon:
        id=randint(1,101)
        sql = f"""INSERT INTO DatosEstadisticos1 (id,contenidoEstadistico) VALUES ({id},?)
            """
        rc  = wcon.cursor().execute(sql,contenido)
        con.commit
        print(str(rc.rowcount),'record inserted ')
        return id

def recuperarDatosEstadisticosBBDD(con,id):
    with con as wcon:
        sql = f"""SELECT contenidoEstadistico FROM DatosEstadisticos1
                  WHERE id = {id}
        """
        res = wcon.execute(sql).fetchall()
        if len(res)==1:
            return res[0][0]

if __name__ == '__main__':
    lista=["hola","caracola"]
   # try:
    fichero_procesar='./src/datos/caracola2.txt'
    con=None
    if GestionFicherosValidacion(fichero_procesar,lista):
        print('Proceso inicia')
        fichero = open(fichero_procesar,'rt',encoding='UTF-8')
        contenido = fichero.read()
        con=connectBBDD();
        if (con!=None):
            id=insertarDatosEstadisticosBBDD(con,contenido)
            res=recuperarDatosEstadisticosBBDD(con,id)
            lista=eval(res)
            print(lista)
    else:
        print('proceso no inicia')


    #except Exception as e:
        #print(f'E-0:{e}')
