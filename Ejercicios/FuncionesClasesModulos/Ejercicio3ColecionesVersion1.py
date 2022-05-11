# Ejercicio Colecciones 3

from random import randint

mujeres=[]
hombres=[]

# for n in range(1,101):
#     genero=randint(0,1)
#     if (genero==1):
#         mujeres.append(randint(0,101))
#     else:
#         hombres.append(randint(0,101))
#Las siguientes 3 lineas son equivalentes a las lineas 8,9,10,11,12 y 13        
genero = [randint(0,1) for n in range(1,101)]
mujeres = [randint(0,101) for g in genero if g==1]
hombres = [randint(0,101) for g in genero if g==0]

print(mujeres) #Lista de 0-100
print(hombres) #Lista de 0-100
print("Numero de chicos:",len(hombres))
print("Numero de chicas:",len(mujeres))
mujeres_mayoresedad=len([n for n in mujeres if n>=18])
print("El nº de mujeres mayores de edad es:",mujeres_mayoresedad)
hombres_menoresedad=len([n for n in hombres if n<18])
print("El nº de hombres menores de edad es:",hombres_menoresedad)

edadmenor_mujer=min(mujeres)
print(f"La(s) mujer(es) con menor edad tiene(n) {edadmenor_mujer} años")
edadmenor_hombre=min(hombres)
print(f"El/Los hombre(s) con menor edad tiene(n) {edadmenor_hombre} años")

edadmayor_mujer=max(mujeres)
print(f"La(s) mujer(es) con mayor edad tiene(n) {edadmayor_mujer} años")
edadmayor_hombre=max(hombres)
print(f"El/Los hombre(s) con mayor edad tiene(n) {edadmayor_hombre} años")

#promedio_edadmujeres=0
#for i in mujeres:
#    promedio_edadmujeres+=i
#print("La edad promedio en las mujeres es:",promedio_edadmujeres//len(mujeres))
promedio_edadmujeres=sum(mujeres)/len(mujeres) # Equivale a las lineas 38,39,40,41
print("La edad promedio en las mujeres es:",promedio_edadmujeres)

#promedio_edadhombres=0
#for i in hombres:
#    promedio_edadhombres+=i
#print("La edad promedio en los hombres es:",promedio_edadhombres//len(hombres))
promedio_edadhombres=sum(hombres)/len(hombres) # Equivale a las lineas 45,46,47 y 48
print("La edad promedio en las hombres es:",promedio_edadhombres)
