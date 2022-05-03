palabra = "Pirata".lower()
countE = 1
count = 0
intento = input("Intenta adivinar palabra: ").lower()
pistas = ["Les Gusta el Oro", "Les Gusta el Mar", "Usan Parches", "Tienen pata de palo"]
while(palabra != intento):

    if(count == len(pistas)):         
        count = 0        
        print(pistas[count])    
    else: 
        print(pistas[count])    
    intento = input(f"Intenta adivinar palabra llevas {countE} fallos: ").lower()    
    countE += 1    
    count += 1