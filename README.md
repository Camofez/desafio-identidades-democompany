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

    API Documentation (Swagger): http://localhost:8000/docs

📂 Estructura del Proyecto
Plaintext

├── backend/
│   ├── main.py            # Lógica central y API
│   ├── Dockerfile         # Receta del contenedor backend
│   ├── requirements.txt   # Dependencias de Python
│   ├── .env               # Variables de configuración
│   ├── test/
│   │   └── test.py        # Pruebas unitarias de identidad
│   └── results/           # CSVs y Logs generados (Persistentes)
├── frontend/
│   ├── index.html         # Interfaz de usuario
│   └── Dockerfile         # Servidor Nginx
└── docker-compose.yml     # Orquestador de servicios

🛡️ Enfoque en Seguridad e Integridad

Durante el desarrollo se implementaron criterios de seguridad proactiva:

    CI/CD Ready: Los contenedores no se despliegan si las pruebas unitarias de pytest fallan, garantizando que nunca se genere una identidad mal formateada.

    Aislamiento: El frontend y el backend operan en redes aisladas dentro de Docker, comunicándose solo por los puertos estrictamente necesarios.