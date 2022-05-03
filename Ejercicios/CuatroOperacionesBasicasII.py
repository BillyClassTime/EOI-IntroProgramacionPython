Op = input("Ingrese operación: ")
try:
    if('+' in Op):
        Op = Op.split('+')
        print(f"El resultado es {float(Op[0]) + float(Op[1])}")
    elif('-' in Op):
        Op = Op.split('-')
        print(f"El resultado es {float(Op[0]) - float(Op[1])}")
    elif('/' in Op):
        Op = Op.split('/')
        print(f"El resultado es {float(Op[0]) / float(Op[1])}")
    elif('*' in Op):
        Op = Op.split('*')
        print(f"El resultado es {float(Op[0]) * float(Op[1])}")
except ValueError:
    print("Por favor, escriba un valor numérico válido")
except ZeroDivisionError:
    print("Error, división entre 0")
except:
    print('un error ha sido detectado')

#Cadenas de caracteres o colección de caracteres.
# 34+40
# Op="34+40"