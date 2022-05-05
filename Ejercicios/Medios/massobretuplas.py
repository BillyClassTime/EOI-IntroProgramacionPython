dias=('Lun','Mar','Mie','Jue','Vie','Sab','Dom')
for dia in dias:
    print(dia)

for dia_numero in enumerate(dias,1):
    print(dia_numero)

#letras=('a','b','c','d','e','fghijklmnoprstuvwxyz')
letras='abcdefghijklmnoprstuvwxyz'

letrasDelAlfabeto=tuple(x for x in letras )
for letra in enumerate(letrasDelAlfabeto,40):
    print("letra:",letra)

#Desempaquetar los valores de la tupla
postres=('tiramisu','flan','pudin')
#unpaking
postrea,postreb,postrec=postres         #Unpacking elementos en la tupla asignados a 
                                        #variables.
nuevospostres=(postrea,postreb,postrec) #Packing de tuplas (Variables asignadas a listas)

print("Postres en la nueva tupla, R=YES:",nuevospostres)

print("Postres en la tupla:",postres)
print("Valores Unpacking",postrea,postreb,postrec)