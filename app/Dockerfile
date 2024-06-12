# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos y la aplicación a /app
COPY requirements.txt .
COPY app.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que la aplicación utilizará
EXPOSE 8000

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]