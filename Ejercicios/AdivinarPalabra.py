palabra1 = "suerte"
print("Adivine la palabra (N para Abandonar): ")
while True:
    palabra2 = input() #.lower() # Ahorrando asignar palabra2 = palabra2.lower()
                               # input.upper()
    if palabra2 == palabra1:
        break # Ahorrando tener una variable boolean comprobando el estado
    elif palabra2 == "N":
        break
    print("Vuelve a intentarlo (N para Abandonar): ")
print("Felicidades, has adivinado la palabra")