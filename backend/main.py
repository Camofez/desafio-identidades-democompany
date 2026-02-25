from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import generate_username
import config
import generate_csv

#1 Configuración inicial: creación de carpeta 'results' y setup de logging
logger, RESULTS_DIR = config.initial_config()

#2 Creación de la aplicación FastAPI y configuración de CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
#3 Endpoint para procesar contratistas y generar correos corporativos
@app.get("/process-contractors")
async def process_contractors():
    logger.info("Inicio del proceso")
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=10)
        users = response.json()
        logger.info(f"Total de registros obtenidos desde el endpoint: {len(users)}")
        
        processed_records = []
        used_usernames = set()
        
        for user in users:
            username = generate_username.generate_username(user['name'], used_usernames)
            record = {
                "Nombre completo": user['name'],
                "Teléfono": user['phone'],
                "Correo electrónico original": user['email'],
                "Empresa para la cual trabaja": user['company']['name'],
                "Ciudad": user['address']['city'],
                "Correo corporativo generado": f"{username}@democompany.com"
            }
            processed_records.append(record)
        
        # 4 Guardar el archivo CSV en la carpeta 'results'
        generate_csv.generate_csv(RESULTS_DIR, record, processed_records)
        
        logger.info("Confirmación de generación del archivo CSV")
        logger.info(f"Total de registros procesados correctamente: {len(processed_records)}")
        
        return {"status": "success", "data": processed_records}
        
    except Exception as e:
        logger.error(f"Error detectado: {str(e)}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)