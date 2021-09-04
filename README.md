# Backend Technical Test

Esta aplicación está desarrollada en python y Django para consumir la api de PokeApi.

## Inicio

Para ejecutar este proyecto se debe crear un entorno virtual.
En la sección de instalación se detallarán los pasos.


### Instalación

Creación de entorno virtual:
```python
python3 -m venv ent01
```

Después de creado el entorno virtual, procederemos activarlo con el siguiente comando:
```python
source ent01/bin/activate
```

Luego procedemos a instalar las librerías y paquetes necesarios para ejecutar el proyecto dentro del entorno virtual. 

Para ello debes usar el siguiente comando:
```python
pip install -r requirements.txt
```

Después procederemos a realizar las migraciones de las tablas:
Para ello debemos escribir el siguiente comando en la terminal.
```python
python manage.py migrate
```

Ahora debemos tener 2 sesiones de la terminal abiertas.

1. Exponer el servicio web para guardar la información del pokémon y poder realizar la busqueda.
```python
python manage.py runserver
```

2. Una vez este corriendo el servicio web, ejecutamos el comando para guardar las diferentes cadenas de evolución.
```python
python main.py
```


Cuando se terminen de cargar las diferentes cadenas de evolución deseadas,
vamos a la siguiente dirección que puedes copiar en tu navegador favorito:
```python
http://localhost:8000/search-pokemon/
```

## Autores

* ** John Fredy García Sáenz ** - *Web Developer*

