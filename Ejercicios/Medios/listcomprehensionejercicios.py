#Ejer N 1
"""
lst1=[1,2,3,4,5]
#lst2=[]
#for n in lst1:
#    lst2.append(n)
lst2=[n for n in lst1 ]
print(lst2)
"""

"""
#Ejer N 2 
rng=[]
for n in range(1200,2001,130):
    rng.append(n)
#print(rng.__str__)
#print(rng[1])
#print(list(rng))
lst=[]
for x in rng:
    lst.append(x)
print(lst)

rng=range(1200,2001,130)  #es equivalente a las lineas 12,13 y 14
lst=[x for x in rng ]     #es equivalente a las lineas 18,19 y 20 
print(lst)                #esto es igual a la linea 21
"""

#Ejer N 3
"""
lst1=[44,54,64,74,104]
lst2=[]
for n in lst1:
    lst2.append(n+6)
print(f"Version larga: Lista 1: {lst1}\nLista 2: {lst2}")


lst1=[44,54,64,74,104]
lst2 = [n+6 for n in lst1] # equivale a las lineas 32, 33 y 34
print(f"Version corta: Lista 1: {lst1}\nLista 2: {lst2}")
"""

#Ejer N 4
"""
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[(num**2) for num in lst1]
print(lst2)
"""

#Ejer N 5
"""
lst1=[2, 4, 6, 8, 10, 12, 14]
lst2=[]
for x in lst1:
    if (x**2)>50:
        lst2.append(x**2)
print(lst2)
lst2=[(x**2) for x in lst1 if (x**2)>50] #equivale a las lineas 52,53,54 y 55
print(lst2)  #igual a la linea 56
"""
#Ejer N 6
"""
dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
#Respuesta.
lst=[n.upper() for n in dict if dict[n]<1300]
print(lst)
"""

#Ejer N 7
"""
#dict={"NY": "Nueva York", "FL": "Finlandia", "CA": "Canada", "VT": "Vietnam"} 
lst=["NY", "FL", "CA", "VT"]
#Version Larga
dict={}
for n in lst:
    #dict.setdefault(n,n)
    dict[n]=n
print(dict)

#Escriba su respuesta aquí.
#Versión corta con comprension de listas
dic={n:n for n in lst}
print(dict)
"""

#Ejer N 8
"""
rng=range(100,160+1,10)
#Version Larga
dict={}
for x in rng:
    dict[x]=(x/100)
print(dict)
#Version con list comprehesion    
dict={x:(x/100) for x in rng} #equivale a las lineas 89,90,91
print(dict)
"""
#Ejer N 9 
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
for n in dict1:
    if dict1[n]>2000:
        dict2[n]=dict1[n]
print(dict2)
#dict2={n:dict1[n] for n in dict1 if dict1[n]>2000}
dict2={x:dict1.get(x) for x in dict1 if dict1.get(x) > 2000}
print(dict2)
