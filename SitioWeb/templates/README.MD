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

# SitioWeb - Entorno de Desarrollo con Docker

Este proyecto está estandarizado con Docker para asegurar que todos los miembros del equipo trabajen exactamente bajo el mismo entorno (Python 3.12 y Django 6.1.1).

---

## 🚀 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu computadora:

1. [Git](https://git-scm.com/)
2. [VS Code](https://code.visualstudio.com/)
3. [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Asegúrate de que la virtualización/WSL2 esté activa en Windows)

---

## 🛠️ Pasos para Iniciar el Proyecto

### 1. Clonar el Repositorio

Abre la terminal de tu computadora e ingresa:

```bash
git clone <URL_DE_TU_REPOSITO_EN_GITHUB>
cd SitioWeb