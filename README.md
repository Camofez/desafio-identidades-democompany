# Identity Management System - DemoCompany Challenge

Este proyecto es una solución integral para la automatización y gestión de identidades corporativas de DemoCompany. El sistema procesa información de contratistas externos, normaliza sus datos y genera perfiles de acceso estandarizados siguiendo las mejores prácticas de IAM (Identity and Access Management).

🚀 Características Principales

    Backend Robusto: Desarrollado con FastAPI, enfocado en alto rendimiento y validación de tipos.

    Normalización Inteligente: Manejo automático de tildes, eñes y caracteres especiales (Unicode a ASCII) para asegurar compatibilidad con sistemas legados.

    Lógica de Identidades: Generación de correos corporativos basados en la inicial del nombre y el apellido, con manejo automático de duplicidades mediante numeración correlativa.

    Restricción de métodos HTTP (CORS) siguiendo el principio de menor privilegio.

    Contenerización completa con Docker.

    Auditoría: Generación automática de archivos de resultados (CSV) y logs de ejecución detallados en la carpeta /results.

🛠️ Tecnologías Utilizadas

    Lenguaje: Python 3.13+

    Framework API: FastAPI / Uvicorn

    Frontend/Proxy: Nginx

    Pruebas: Pytest

    Despliegue: Docker & Docker Compose

📦 Instalación y Despliegue

Gracias a la dockerización del proyecto, el despliegue es agnóstico al sistema operativo:

El sistema estará disponible en:

    Frontend: http://localhost

    Backend: http://localhost:8000

📂 Estructura del Proyecto
.
    ├── backend/
    │   ├── main.py                # Servidor FastAPI y lógica de identidades
    │   ├── Dockerfile             # Configuración del contenedor de Python
    │   ├── requirements.txt       # Librerías (fastapi, uvicorn, python-dotenv, etc.)
    │   ├── test/
    │   │   └── test.py            # Pruebas unitarias (Normalización, Duplicados)
    │   └── results/               # Salida de datos (Persistente vía Docker Volumes)
    │       ├── execution.log      # Registro de auditoría de procesos
    │       └── contractors.csv    # Reporte final de identidades generadas
    ├── frontend/
    │   ├── index.html             # Interfaz de usuario (Vanilla JS)
    │   └── Dockerfile             # Configuración del servidor Nginx
    ├── docker-compose.yml         # Orquestador de microservicios
    └── .gitignore                 # Archivos excluidos del repositorio (Logs, .env)

🛡️ Enfoque en Seguridad e Integridad

Durante el desarrollo se implementaron criterios de seguridad proactiva:

    CI/CD Ready: Los contenedores no se despliegan si las pruebas unitarias de pytest fallan, garantizando que nunca se genere una identidad mal formateada.

    Aislamiento: El frontend y el backend operan en redes aisladas dentro de Docker, comunicándose solo por los puertos estrictamente necesarios.