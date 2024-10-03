# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la app al contenedor
COPY . /app/

# Copia el archivo .env al contenedor
COPY .env /app/

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación con gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "FruitAdmin.wsgi"]
