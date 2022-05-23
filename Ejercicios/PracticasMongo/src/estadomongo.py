from pymongo import MongoClient
clientDB = MongoClient('mongodb://localhost:27017/')
db = clientDB.admin
resultado = db.command('serverStatus')
print('Host:',resultado['host'])
print('Version:',resultado['version'])
print('Process:',resultado['process'])