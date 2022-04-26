from datetime import datetime
fecha="10-11-2022"
fecha1=datetime.strptime(fecha,'%m-%d-%Y').date()
print("Fecha1:",fecha1)
print(f"Fecha1 {fecha1.day}/{fecha1.month}/{fecha1.year}")


fecha2=datetime.strptime(fecha,'%m-%d-%Y')
print("Fecha2:",fecha2)

fecha3=datetime.now()
print("Fecha3:",fecha3)
print("Fecha3:",fecha3.strftime("%A %d %b %Y"))
