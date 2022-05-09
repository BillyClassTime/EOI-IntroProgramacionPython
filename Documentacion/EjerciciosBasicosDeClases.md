Ejercicios con Clases

1. Se ha definido una clase que representa un inventario de aviones. También se crea una instancia de esta clase Jet y se asigna a la variable first_item.

   Imprimir el nombre del primer_elemento.

   ```python
   class Jets:
       def __init__(self, name, country):
           self.name = name
           self.origin = country
           
   first_item = Jets("F16", "USA")
   #Escriba su respuesta aquí.
   a=
   print(a)
   ```

2. Ahora imprima el origen del primer_elemento.
   ```python
   class Jets:
       model = None
       country = 0
   
       def __init__(self, name, country):
           self.name = name
           self.origin = country
           
   first_item = Jets("F16", "USA")
   #Escriba su respuesta aquí.
   b=
   
   print(b)
   ```

3. Cree nuevas instancias hasta el sexto elemento siguiendo este orden: F14, SU33, AJS37, Mirage2000, Mig29, A10. 

   Puede tener en cuenta que los orígenes son:

   F14: USA
   SU33: Russia
   AJS37: Sweden
   Mirage2000: France
   Mig29: USSR
   A10: USA

   ```python
   class Jets:
       model = None
       country = 0
       def __init__(self, name, country):
           self.name = name
           self.origin = country
   #Escriba su respuesta aquí.        
   first_item=
   second_item=
   third_item= 
   fourth_item=
   fifth_item=
   sixth_item=
   first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
   print(first_army)
   ```

4. Agregue otro atributo llamado "cantidad" al método de inicialización (generalmente denominado constructor o __init__). 

   Luego defina "asignar" este atributo al atributo self.quantity dentro del constructor.

   Luego cree 2 instancias para: F14 y Mirage2000 con cantidades 87 y 35.

   ```python
   class Jets:
       model = None
       country = 0
       def __init__(self, name, country):
           self.name = name
           self.origin = country
   #Escriba su respuesta aquí.        
   first_item=
   second_item=
   total=
   print(total)
   ```

5. 
   Construir una clase simple desde cero. Ya se ha creado una instancia para usted y los atributos de la instancia se incluyen dentro del print. Tome esas pistas y con estos datos cree la clase.

   ```python
   #Escriba su respuesta aquí.
   
   
   
   
   
   nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
   print(nq2019.category, nq2019.year, nq2019.winner)
   
   ```

6. Construir una clase simple desde cero. Es la misma que el ejercicio anterior, ahora usará la función __ __str__ __  para devolver una representación de cadena para la clase cuando sea necesario.

   ```python
   #Escriba su respuesta aquí.
   
   
   
   
   
   nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
   ```

7. 
   Cree una clase llamada **myfunc** y dentro de ella coloque una función muy simple llamada "quinta" que toma x y devuelve la quinta potencia de x. No se necesitan __init__ o atributos de clase.


   Finalmente llame a su función con el número 5 y asígnela a la variable ans.

   ```python
   #Escriba su respuesta aquí.
    
   
   
   ans=
   print(ans)
   ```

8. Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.


   Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".


   También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.


   Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.

   
   ```python
   #Escriba su respuesta aquí.
   
   
    
   
   
   ans1 = myfunc.ElevarAlaPotencia(5, 6)
   ans2 = 
   
   print(ans1)
   print(ans2)
   ```


