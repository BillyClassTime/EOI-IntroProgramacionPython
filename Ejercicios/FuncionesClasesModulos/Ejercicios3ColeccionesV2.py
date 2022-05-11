from random import randint
dataset = list(
        {
            "gender": "F" if randint(0, 1) == 0 else "M",
            "age": randint(0, 120),
        }
        for _ in range(100)
    )
#print(dataset)
mujeres_mayores_edad= len(
        [
            person
            for person in dataset
            if person["gender"] == "F" and person["age"] >= 18
        ]
    )
print(f"Número de mujeres mayores de edad: {mujeres_mayores_edad}")
hombres_menores_edad= len(
        [
            person
            for person in dataset
            if person["gender"] == "M" and person["age"] < 18
        ]
    )
print(f"Número de hombres menores de edad: {hombres_menores_edad}")
hombres_menor_edad= min(
        [
            person["age"]
            for person in dataset
            if person["gender"] == "M"
        ]
    )
print(f"La edad menor entre los hombres es: {hombres_menor_edad}")
mujeres_menor_edad= min([person["age"] for person in dataset if person["gender"] == "F"])
print(f"La edad menor entre las mujeres es: {mujeres_menor_edad}")
total_hombres= len([person for person in dataset if person["gender"] == "M" ])
total_mujeres= 100 - total_hombres
hombres_suma_edades= sum([person["age"]  for person in dataset  if person["gender"] == "M" ] )
mujeres_suma_edades= sum(
        [
            person["age"]
            for person in dataset
            if person["gender"] == "F"
        ]
    )
print(f"El promedio de la edad de los chicos es:{hombres_suma_edades/total_hombres}")
print(f"El promedio de la edad de las chicas es:{mujeres_suma_edades/total_mujeres}")
