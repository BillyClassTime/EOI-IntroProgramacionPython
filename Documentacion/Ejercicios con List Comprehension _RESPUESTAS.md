Ejercicios con List Comprehension

1. Cree una lista idéntica a partir de la primera lista utilizando la comprensión de listas.

   ```python
   lst1=[1,2,3,4,5]
   
   #Respuesta.
   
   lst2 = [i for i in lst1]
   
   print(lst2)
   ```

2. Crear una lista a partir de los elementos de un rango de 1200 a 2000 con pasos de 130, utilizando la comprensión de listas.

   ```python
   #Respuesta.
   
   rng = range(1200, 2000, 130)
   lst = [i for i in rng]
   
   print(lst)
   ```

3. Use la comprensión de listas para construir una nueva lista, pero agregue 6 a cada elemento.
   ```python
   #Respuesta.
   
   lst1=[44,54,64,74,104]
   
   lst2 = [i+6 for i in lst1]
   
   print(lst2)
   ```
4. Utilizando la comprensión de listas, construya una lista a partir de los cuadrados de cada elemento de la lista.
   ```python
   lst1=[2, 4, 6, 8, 10, 12, 14]
   
   #Respuesta.
   
   lst2 = [i**2 for i in lst1]
   
   print(lst2)
   
   ```
5. Utilizando la comprensión de listas, construya una lista a partir de los cuadrados de cada elemento de la lista, si el cuadrado es mayor que 50.
   ```python
   lst1=[2, 4, 6, 8, 10, 12, 14]
   
   #Respuesta.
   
   lst2 = [i**2 for i in lst1 if i**2>50]
   
   print(lst2)
   ```
6. El diccionario dado consta de vehículos y sus pesos en kilogramos. Construya una lista de nombres de vehículos con peso inferior a 1300 kilogramos. En la misma lista de comprensión, haga que los nombres de las claves estén en mayúsculas.
   ```python
   
   dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}
   
   #Respuesta.
   
   lst = [i.upper() for i in dict if dict[i]<1300]
   
   print(lst)
   
   ```
   
7. Cree un diccionario de la lista con los mismos pares clave:valor, como: {"clave": "clave"}.

   ```python
   lst=["NY", "FL", "CA", "VT"]
   
   #Respuesta.
   
   dict = {i:i for i in lst}
   
   
   print(dict)
   ```

8. Cree un rango de 100 a 160 con paso 10.   Utilizando la comprensión de listas, cree un diccionario en el que cada número del rango sea la clave y cada elemento dividido por 100 sea el valor.

   ```python
   #Respuesta.
   rng = range(100, 160, 10)
   dict = {i:i/100 for i in rng}
   
   print(dict)
   ```
   
   ​    
   
9. Usando la comprensión de listas y un argumento condicional, cree un diccionario a partir del diccionario actual donde solo los pares clave:valor con un valor superior a 2000 se toman en el nuevo diccionario.

   ```python
   dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
   #Respuesta.
   dict2 = {i:dict1[i] for i in dict1 if dict1[i]>2000}
   
   
   print(dict2)
   ```
   
   



 



