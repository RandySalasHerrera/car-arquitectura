# Prueba tecnica car de arquitectura
El proyecto consiste en desarrollar una aplicación Django para un que permita importar y gestionar datos relacionados con los estudiantes, profesores, cursos, calificaciones. Se utilizará Celery para procesar las importaciones masivas de datos, y se implementará un scrapper para obtener información adicional sobre los cursos desde una fuente externa.

## Requisitos

Asegúrate de tener los siguientes requisitos instalados en tu máquina local:

- Docker
- Docker Compose
- Git

## Clonación del Repositorio

1. Abre una terminal y navega hasta el directorio donde deseas clonar el repositorio.
2. Ejecuta el siguiente comando para clonar el repositorio:

   ```shell
   git clone https://github.com/RandySalasHerrera/car-arquitectura.git

## Configuración y Uso
Sigue los pasos a continuación para configurar y utilizar la aplicación:

1. Abre una terminal y navega hasta el directorio raíz de la aplicación clonada.

2. Construye la imagen de Docker ejecutando el siguiente comando:  
   ```shell
   docker compose build
3. Inicia el contenedor de Docker ejecutando el siguiente comando:
    ```shell
   docker compose up -d
4. Crear el super usuario para poder iniciar sesion en el admin:
    ```shell
   docker compose run web python manage.py createsuperuser
5. Accede a la aplicación en tu navegador web utilizando la siguiente URL:
   ```shell
   http://localhost:8000
6. ¡Listo! Ahora puedes utilizar y explorar la aplicación.

## Importar archivo excel
Para poder acceder a la vista de importacion debes usar la siguiente URL: http://localhost:8000 ten encuenta que debes usar el archivo import.xlsx que se encuentra en la raiz de este proyecto

## Scrapper de cursos
Para poder acceder a la vista del scraper de cursos debes usar la siguiente URL: 
http://localhost:8000/scraper 

## Admin
Para poder acceder a la vista del administrador debes usar la siguiente URL: http://localhost:8000/admin/ 


