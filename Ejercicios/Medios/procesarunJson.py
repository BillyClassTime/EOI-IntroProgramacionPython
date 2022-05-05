import json
# jsonventas = json.loads("ORIGIN DE LOS DATOS DEL JSON")
jsonventas = '{"departamento":8,"nombredepto":"Ventas","director":"Juan Rodriguez","empleados":[{"nombre":"Pedro","apellido":"Fernandez"},{"nombre":"Jacinto","apellido":"Benavente"}]}'
#segundoJson= "{'departamento':8,'nombredepto':'Ventas','director':'Juan Rodriguez','empleados':[{'nombre':'Pedro','apellido':'Fernandez'},{'nombre':'Jacinto','apellido':'Benavente'}]}"
#tercerJson = "{\"departamento\":8,\"nombredepto\":\"Ventas\",\"director\":\"Juan Rodriguez\",\"empleados\":[{\"nombre\":\"Pedro\",\"apellido\":\"Fernandez\"},{\"nombre\":\"Jacinto\",\"apellido\":\"Benavente\"}]}"
#print(jsonventas)
print(type(jsonventas))

datosDepartamento = json.dumps(jsonventas)
print(type(datosDepartamento))

jsonventas = json.loads(datosDepartamento)
print(type(jsonventas))
#datosSegundoDepto = json.dumps(segundoJson)
#datostercerDepto  = json.dumps(tercerJson)

print("Json 1:",datosDepartamento)
#print("Json 2:",datosSegundoDepto)
#print("Json 3:",datostercerDepto)

# Conclusion: 
# la variable que debo utilizar para procesar el JSON como una coleccion compleja (compuesta) es el deserializado (loads)
for val in jsonventas:
     print (val)

# for val in datosDepartamento:
#     print(val)

