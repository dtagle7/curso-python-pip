# especificamos que version de Python deseamos utilizar  
FROM python:3.8

# el workdir sera la raiz de nuestro contenedor, en este caso la raiz sera /app
WORKDIR /app
# vamos a copiar el archivo requeriments.txt de nuestra computadora hacia la ruta /app del contenedor
COPY requirements.txt /app/requirements.txt

# instalar las librerias y dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copiar todos los archivos de la carpeta de donde levantamos el contenedor hacia la ruta /app del contenedor
COPY . /app

# comando bash que permite mantener activo el contenedor
CMD bash -c "while true; do sleep 1; done"