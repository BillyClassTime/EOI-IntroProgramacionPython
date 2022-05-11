class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country
        if Jets.model==None:
            Jets.model = 1
        else:
            Jets.model += 1
        Jets.country +=1
        
first_item = Jets("F16", "USA")
first_item=Jets("F14","USA")
second_item=Jets("SU33","Russia")
third_item=Jets("AJS37","Sweden")
fourth_item=Jets("Mirage2000","France")
fifth_item=Jets("Mig29","USSR")
sixth_item=Jets("A10","USA")

#Escriba su respuesta aquí.
b=first_item.origin
print(b)

print(Jets.model)
print(Jets.country)