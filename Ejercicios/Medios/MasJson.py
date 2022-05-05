import json

deptoVentas='{"departamento":8,"nombredepto":"Ventas","director":"Juan Rodriguez","empleados":[{"nombre":"Pedro","apellido":"Fernandez"},{"nombre":"Jacinto","apellido":"Benavente"}]}'

objeto_deptoVentas = json.loads(deptoVentas)

print(type(objeto_deptoVentas))

for elem in objeto_deptoVentas:
    if elem != "empleados":
        print(elem,objeto_deptoVentas[elem])
    else:
        print('Integrantes del departmento')
        for integrantesDepto in objeto_deptoVentas['empleados']:
            #print('\t\t',integrantesDepto["nombre"],integrantesDepto['apellido'])
            #print(integrantesDepto,objeto_deptoVentas[integrantesDepto]) ESTO FALLA
            #print(integrantesDepto) Muestra: {'nombre': 'Pedro', 'apellido': 'Fernandez'}
            print('\t',integrantesDepto['nombre'])
            print('\t',integrantesDepto['apellido'])