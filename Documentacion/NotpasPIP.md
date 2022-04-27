# Instalar PIP

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py get-pip.py
```

Variables del sistema

```
C:\Users\REPLAZAR POR VUESTRO USUARIO\AppData\Local\Programs\Python\Python310\Scripts
```

Actualizar pip

```
py -m pip install –U pip
```

Comprobar (Deberan existir los modulos datetime y locale, entre otros)

```
py
help('modules')
```

Instalar el módulo para las zonas horarias

```
pip install pytz
```

Verificar que ha quedado instalado en Python

```
py
help('modules')
```

