Ejercicios con Clases

1. Se ha definido una clase que representa un inventario de aviones. También se crea una instancia de esta clase Jet y se asigna a la variable first_item.

   Imprimir el nombre del primer_elemento.

   ```python
   class Jets:
       def __init__(self, name, country):
           self.name = name
           self.origin = country
           
   first_item = Jets("F16", "USA")
   #Respuesta.
   a=first_item.name
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
   #Respuesta.
   b=first_item.origin
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
   #Respueta.        
   first_item=Jets("F14", "USA")
   second_item=Jets("SU33", "Russia")
   third_item=Jets("AJS37", "Sweden")
   fourth_item=Jets("Mirage2000", "France")
   fifth_item=Jets("Mig29", "USSR")
   sixth_item=Jets("A10", "USA")[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
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
   #Respuesta.       
   first_item=Jets("F14","USA",87)
   second_item=Jets("Mirage2000","France",35)
   total = first_item.quantity+second_item.quantity
   print(total)
   ```

5. 
   Construir una clase simple desde cero. Ya se ha creado una instancia para usted y los atributos de la instancia se incluyen dentro del print. Tome esas pistas y con estos datos cree la clase.

   ```python
   #Respuesta.
   class Nobel:
       def __init__(self, categoria, año, ganador):
           self.categoria = categoria
           self.año = año
           self.ganador = ganador
   nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
   print(nq2019.categoria, nq2019.año, nq2019.ganador)
   ```

6. Construir una clase simple desde cero. Es la misma que el ejercicio anterior, ahora usará la función __ __str__ __  para devolver una representación de cadena para la clase cuando sea necesario.

   ```python
   #Respuesta.
   class Nobel:
       def __init__(self, categoria, año, ganador):
           self.categoria = categoria
           self.año = año
           self.ganador = ganador
       def __str__(self):
           return "{} fué el ganador del Nobel de {} en {}".format(self.ganador, self.categoria, self.año)
   
   nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
   print(nq2019)
   ```

7. 
   Cree una clase llamada **myfunc** y dentro de ella coloque una función muy simple llamada "quinta" que toma x y devuelve la quinta potencia de x. No se necesitan __init__ o atributos de clase.


   Finalmente llame a su función con el número 5 y asígnela a la variable ans.

   ```python
   #Respuesta.
   class myfunc:
       def quinta(x):
           return x**5
   ans = myfunc.quinta(5)
   print(ans)
   ```

8. Ahora hagamos algunos cambios en la clase que creamos en el ejercicio anterior de Python.


   Primero haga su función para que tome los parámetros: x e y. x será el número que se eleva, e será la potencia. ¡Entonces, los usuarios pueden elevar los números a cualquier potencia! También cambiemos el nombre de la función a "ElevarAlaPotencia".


   También agreguemos una representación de cadena rápidamente, de modo que cuando un usuario imprima la clase obtenga una descripción significativa.


   Puede ser algo como: Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia.

   ```python
   #Respuesta.
   class myfunc:
   
       def ElevarAlaPotencia(x,y):
           return x**y
   
       def __str__(self):
           return "Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia."
   
   ans1 = myfunc.ElevarAlaPotencia(5, 6)
   ans2 = myfunc()
   
   print(ans1)
   print(ans2)
   ```


