def initial_config():
    import os
    import logging
    # 1. Crear la carpeta 'results' si no existe
    RESULTS_DIR = "results"
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    # 2. Configuración de logs guardando en la carpeta 'results'
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(RESULTS_DIR, "execution.log")),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    return logger, RESULTS_DIR