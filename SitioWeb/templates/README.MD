# Proyecto Sitio Web Django

Este es el repositorio del proyecto en equipo para SitioWeb.

## Requisitos previos

Tener instalado Python 3.13 o superior.

## Configuración para colaborar

Sigue estos pasos la primera vez que clones este proyecto:

1. **Crear el entorno virtual:**
   ```bash (en el cmd)
   python -m venv venv

   Activar el entorno virtual:

En Windows (PowerShell): venv\Scripts\activate

En Mac/Linux: source venv/bin/activate

Instalar las dependencias:

Bash


pip install -r requirements.txt
Crear la base de datos local:

Bash


python manage.py migrate
Iniciar el servidor local:

Bash


python manage.py runserver

---

Una vez que guardes ambos archivos, **`.gitignore`** se encargará de que las carpetas pesadas (`venv`, `.venv`) y la base de datos (`db.sqlite3`) no se suban cuando ejecutes los comandos de Git.