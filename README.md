# Investigacion_Lenguajes
Para ejecutar el proyecto hacer lo siguiente:
En la consola de VS Code ejecutar los siguientes comandos.
* python -m venv my-venv

Luego de crear la carpeta que contiene el entorno virtual, procederemos a navegar detro de ella hasta scripts, para llegar scripts, dentro de la carpeta Proyecto ejecutamos los siguientes comandos en consola
* cd my-venv
* cd scripts

Para poder activar nuestro entorno virtual, ejecutaremos el siguiente comando que permite activar el entorno virtual

* Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Luego dentro de la carpeta scripts ejecutamos lo siguiente

* ./activate

Una vez tengamos nuestro entorno virtual listo, instalamos los siguientes paquetes

* pip install tweepy 
* pip install flask
* pip install mysql-connector-python

Una vez instalados los paquetes, procedemos a salir de la carpeta de scripts desde la terminal

Y luego, desde la misma terminal de VS Code nos dirigimos a donde se encuentra el archivo para correr el archivo

* python prueba.py
Para poder ejecuarlo
