#ListasDeComprensionEnPython.py
frutas=['manzana','banana','cherry','kiwi','mango',]
"""
nueva_lista=[]
for fruta in frutas:
    if "a" in fruta:
        nueva_lista.append(fruta)
"""
nueva_lista = [fruta for fruta in frutas if "a" in fruta]
print(nueva_lista)