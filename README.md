# Personal Suite

**Personal Suite** is an experimental project designed to centralize everyday tasks in a single application.  
It aims to offer modules for personal finance management, media tracking (movies, series, YouTube videos), and more, all from one place.  

This repository is also intended as a learning and portfolio project, where I share how I approach software development decisions regarding **architecture, technologies, and organization**.

<details>
<summary>🇪🇸 Español</summary>

**Personal Suite** es un proyecto experimental diseñado para centralizar tareas cotidianas en una sola aplicación.  
Ofrece módulos para gestión de finanzas personales, seguimiento de medios (películas, series, videos de YouTube), y más, todo desde un mismo lugar.

Este repositorio también sirve como proyecto de aprendizaje y portafolio, donde comparto cómo tomo decisiones de desarrollo de software respecto a **arquitectura, tecnologías y organización**.

</details>

---

## 📋 Features / Características

- Modular architecture (each feature as a plugin/module).
- Modules can be private, as there are no hardcoded references, and the core loads them dynamically.
- Core service with FastAPI + SQLAlchemy/SQLModel.
- PostgreSQL as the main database.
- Example module: Media Tracker (track Movies, TV Shows, YouTube videos, etc.).
- Docker Compose support for local development and deployment.

<details>
<summary>🇪🇸 Español</summary>

- Arquitectura modular (cada funcionalidad como plugin/módulo).
- Los módulos pueden mantenerse privados, ya que no hay referencias hardcodeadas y el core los carga de manera dinámica.
- Servicio core con FastAPI + SQLAlchemy/SQLModel.
- PostgreSQL como base de datos principal.
- Módulo de ejemplo: Media Tracker (seguimiento de películas, series, vídeos de YouTube, etc.).
- Soporte para Docker Compose para desarrollo y despliegue local.

</details>

---

## 🛠️ Tech Stack / Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/) – API framework.
- [SQLAlchemy / SQLModel](https://sqlmodel.tiangolo.com/) – ORM and database models.
- [Pydantic](https://pydantic.dev/) – Data validation.
- [Uvicorn](https://www.uvicorn.org/) – ASGI server.
- [psycopg2](https://www.psycopg.org/) – Synchronous PostgreSQL adapter for Python, as the project is designed to be synchronous.
- [PostgreSQL](https://www.postgresql.org/) – Database.
- [Docker & Docker Compose](https://docs.docker.com/) – Containerization.
- Python 3.13 (tested).

<details>
<summary>🇪🇸 Español</summary>

- [FastAPI](https://fastapi.tiangolo.com/) – Framework para APIs.
- [SQLAlchemy / SQLModel](https://sqlmodel.tiangolo.com/) – ORM y modelos de base de datos.
- [Pydantic](https://pydantic.dev/) – Validación de datos.
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI.
- [psycopg2](https://www.psycopg.org/) – Adaptador síncrono de PostgreSQL para Python, ya que el proyecto está diseñado para ser síncrono.
- [PostgreSQL](https://www.postgresql.org/) – Base de datos.
- [Docker & Docker Compose](https://docs.docker.com/) – Contenerización.
- Python 3.13 (probado).

</details>

---

## 1️⃣ Getting Started / Comenzando

### Environment Setup / Configuración del Entorno
Currently, these are the environment variables used in the project, although only `DATABASE_URL` is required to run the application:

- `DATABASE_URL`: PostgreSQL connection string (e.g., `postgresql+psycopg2://user:password@localhost/dbname`).
- `UVICORN_HOST`: Host for Uvicorn (default: `0.0.0.0`), which allows access from all network interfaces.
- `UVICORN_PORT`: Port for Uvicorn (default: `8000`).
- `UVICORN_RELOAD`: Whether to enable auto-reload (default: `true` for development).
- `ENGINE_ECHO`: Enable SQLAlchemy logging (default: `false`).

<details>
<summary>🇪🇸 Español</summary>

Actualmente, estas son las variables de entorno utilizadas en el proyecto, aunque solo `DATABASE_URL` es obligatoria para ejecutar la aplicación:

- `DATABASE_URL`: Cadena de conexión a PostgreSQL (ej.: `postgresql+psycopg2://usuario:contraseña@localhost/nombre_bd`).
- `UVICORN_HOST`: Host para Uvicorn (por defecto `0.0.0.0`), permite acceso desde todas las interfaces de red.
- `UVICORN_PORT`: Puerto para Uvicorn (por defecto `8000`).
- `UVICORN_RELOAD`: Activar recarga automática (por defecto `true` para desarrollo).
- `ENGINE_ECHO`: Activar logging de SQLAlchemy (por defecto `false`).

</details>

### Prerequisites / Prerrequisitos
- Python 3.13
- PostgreSQL
- Docker & Docker Compose (for local deployment / Para despliegue local)

### Clone the Repository / Clonar el Repositorio
To get a copy of this project, run the following command in your terminal:

<details>
<summary>🇪🇸 Español</summary>

Para obtener una copia de este proyecto, ejecuta:

</details>

```bash
git clone https://github.com/jruizg22/personalsuite-backend-core.git
cd personalsuite-backend-core
```

### Install Dependencies / Instalar Dependencias
It's recommended to use a virtual environment. You can create and activate one using:

<details>
<summary>🇪🇸 Español</summary>

Se recomienda crear un entorno virtual, puedes crearlo y activarlo con:

</details>

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Then, install the required packages from `pyproject.toml`:

<details>
<summary>🇪🇸 Español</summary>

Instala las dependencias usando `pyproject.toml`:

</details>

```bash
pip install .
```

### Running the Application / Ejecutar la Aplicación
You can run the application using Uvicorn with the following command:

<details>
<summary>🇪🇸 Español</summary>

Puedes ejecutar la aplicación usando Uvicorn:

</details>

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Or, alternatively, just run the main.py file:

<details>
<summary>🇪🇸 Español</summary>

O simplemente ejecuta el archivo principal:

</details>

```bash
python main.py
```

---

## 🔌 Available Modules / Módulos Disponibles

The **Personal Suite** core is designed to be modular. Each feature can exist as a separate module/plugin, which the core loads dynamically at runtime. This allows you to add or remove functionality without modifying the core application.

Currently available modules:

- [Media Tracker](https://github.com/jruizg22/personalsuite-backend-mediatracker) – Track Movies, TV Shows, and YouTube videos. (WIP)

<details>
<summary>🇪🇸 Español</summary>

El **core de Personal Suite** está diseñado para ser modular. Cada funcionalidad puede existir como un módulo o plugin independiente, que el core carga dinámicamente en tiempo de ejecución. Esto permite añadir o quitar funcionalidades sin modificar la aplicación principal.

Módulos disponibles actualmente:

- [Media Tracker](https://github.com/jruizg22/personalsuite-backend-mediatracker) – Para seguimiento de películas, series y vídeos de YouTube. (En progreso)

</details>

---

### Installing modules / Instalar módulos

To install a module, follow these steps:

1. Download or clone the module repository.
2. Install the module using pip. I recommend using absolute paths, but if you use relative paths keep in mind where the module root directory is. For example, `pip install /rute/to/module/module_root`.
3. The core will automatically detect and import all modules installed in the environment at startup.

<details>
<summary>🇪🇸 Español</summary>

Para instalar un módulo, sigue estos pasos:

1. Descarga o clona el repositorio del módulo.
2. Instala el módulo usando `pip`. Recomiendo usar rutas absolutas, pero si usas rutas relativas ten en cuenta dónde se encuentra el directorio raíz del módulo. Por ejemplo: `pip install /ruta/al/modulo/modulo_raiz`.
3. El core detectará e importará automáticamente todos los módulos instalados en el entorno al iniciar la aplicación.

</details>

---

### Uninstalling modules / Desinstalar módulos

If you want to remove a module from your environment, follow these steps:

1. Identify the module name or path installed in your environment.
2. Uninstall the module using pip:

```bash
pip uninstall module_name
```
3. Restart the core application. The module will no longer be available.

<details>
<summary>🇪🇸 Español</summary>

Si deseas eliminar un módulo de tu entorno, sigue estos pasos:

1. Identifica el nombre o la ruta del módulo instalado en tu entorno.
2. Desinstala el módulo usando pip:
```bash
pip uninstall nombre_modulo
```
3. Reinicia la aplicación core. El módulo ya no estará disponible.


</details>

---

## 🐋 Deployment / Despliegue
For deployment, you can configure the image with the `Dockerfile` and use Docker Compose with the provided `docker-compose.yaml` file.

<details>
<summary>🇪🇸 Español</summary>

Para desplegar, puedes configurar la imagen usando el `Dockerfile` y usar Docker Compose con el archivo `docker-compose.yaml` incluido.

</details>

### Dockerfile
This file contains the settings to build the Docker image. By default, it only includes the core app, which doesn't do much without modules.

To include modules in your Docker image, you need to make sure that each module is copied into the container and installed.

1. Use the `COPY` instruction to add the module folder into the image. For example:   
```dockerfile
COPY personalsuite-backend-mediatracker/ ./modules/mediatracker/
```
Keep in mind, `personalsuite-backend-mediatracker` is the root directory of the module, so be mindful about the path.

2. Use the `RUN` instruction to install the module in the core environment using pip:
```bash
RUN pip install ./modules/mediatracker/
```

The Dockerfile also contains comments about it.

<details>
<summary>🇪🇸 Español</summary>

Este archivo contiene la configuración para construir la imagen de Docker. Por defecto, solo incluye la aplicación core, que no hace mucho sin los módulos.

Para incluir módulos en tu imagen de Docker, asegúrate de copiar cada módulo dentro del contenedor e instalarlo:

1. Usa la instrucción `COPY` para añadir la carpeta del módulo a la imagen. Por ejemplo:  
```dockerfile
COPY personalsuite-backend-mediatracker/ ./modules/mediatracker/
```
Ten en cuenta que `personalsuite-backend-mediatracker` es el directorio raíz del módulo, así que cuidado con la ruta.

2. Usa la instrucción `RUN` para instalar el módulo en el entorno del core usando pip:
```bash
RUN pip install ./modules/mediatracker/ 
```

El Dockerfile también contiene comentarios sobre cómo hacerlo.

</details>

### Building the image and running the container / Construir la imagen y arrancar el contenedor

To build the image and run the container, use:

<details>
<summary>🇪🇸 Español</summary>

Para desplegar usando Docker Compose, usa el archivo `docker-compose.yaml` incluido.  

Para construir la imagen y arrancar el contenedor, usa:

</details>

```bash
docker-compose up --build
```

To stop and remove the container:

<details>
<summary>🇪🇸 Español</summary>

Para detener y eliminar el contenedor:

</details>

```bash
docker-compose down
```