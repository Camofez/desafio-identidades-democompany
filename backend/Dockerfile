# Etapa 1: Construcción y Pruebas
FROM python:3.13-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Ejecutar pruebas antes de continuar
# Si falla aquí, la construcción se detiene
RUN pytest test/test.py

# Etapa 2: Imagen Final (solo si la anterior tuvo éxito)
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /app /app

EXPOSE 8000
CMD ["python", "main.py"]