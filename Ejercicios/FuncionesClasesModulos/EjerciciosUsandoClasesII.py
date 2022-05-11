class Jets:
    def __init__(self, name, country,cantidad=0):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

    def __str__(self):
        return "{}->{}".format(self.name, self.origin)

first_item = Jets("F16", "USA")
#Escriba su respuesta aquí.
a=first_item.name
b=first_item.origin
print(a)
print(b)
first_item=Jets("F14","USA")
second_item=Jets("SU33","Russia")
third_item=Jets("AJS37","Sweden")
fourth_item=Jets("Mirage2000","France")
fifth_item=Jets("Mig29","USSR")
sixth_item=Jets("A10","USA")
#first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
first_army=["avion:{}".format(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]
#first_army=[first_item,second_item,third_item,fourth_item,fifth_item,sixth_item]
#print(first_item)
print("Avion:",first_item)
print(first_army)
#['F14->USA', 'SU33->Russia', 'AJS57->Sweden'...]
first_item=Jets('F14',"USA",87)
second_item=Jets('Mirage2000',"France",35)
total=first_item.cantidad + second_item.cantidad
print("Respuesta ejercicio 4:",total)