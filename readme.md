# CRUD - Django
Este es un pequeño proyecto realizado con el framework de Django para desarrollo web, Aquí se presenta una simple aplicación para ejemplificar un CRUD completo y mostrar varias de las funcionalidades que Django tiene para ofrecer.

## Tecnologías:
- Python
- Django
- HTML
- Jinja2

## Crear variables de entorno (archivo .env) Para conexion a MYSQLo
   MYSQL_HOST = ""
   MYSQL_USER = ""
   MYSQL_PASSWORD = ""
   MYSQL_PORT = ""
   MYSQL_DB = ""

## Ingreso al administrador del sistema
   
   link: http://127.0.0.1:8000/admin/

   Usuario: admin
   Contraseña: *Admin123


## ¿Como correr el proyecto?
**1:** Clonar el repositorio con el comando de git:
```
git clone <dirección del repo>
```
**2:** Ingresar desde la terminal dentro de la carpeta del proyecto. Ejemplo en linux:
```
cd <nombre del directorio>
```
**3:** Crear un entorno virtual:
```
python -m venv venv
```
**4:** Ingresar en el entorno virtual:
- Para linux y Mac:
```
source venv/bin/activate
```
- Para Window:
```
venv\Scripts\activate.bat
```
**5:** Descargar las dependencias del archivo 'requirements.txt' con el comando:
```
pip install -r requirements.txt   
```
**6:** Ingresar en la carpeta del proyecto Django:
```
cd <nombre del proyecto Django>
```
**7:** Ejecutar el servidor de desarrollo de Django:
```
python manage.py runserver
```
**8:** En el navegador ir al localhost:8000.


