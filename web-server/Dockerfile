# especificamos que version de Python deseamos utilizar  
FROM python:3.10

# el workdir sera la raiz de nuestro contenedor, en este caso la raiz sera /app
WORKDIR /app
# vamos a copiar el archivo requeriments.txt de nuestra computadora hacia la ruta /app del contenedor
COPY requirements.txt /app/requirements.txt

# instalar las librerias y dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copiar todos los archivos de la carpeta de donde levantamos el contenedor hacia la ruta /app del contenedor
COPY . /app

# comando para lanzar el servidor de uvicorn enviando el nombre del archivo con el codigo fuente y la instancia de FastAPI, IP y puerto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
