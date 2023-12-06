# Usamos una imagen base
FROM ubuntu:latest

# Etiqueta de información del creador
LABEL maintainer="nicotalavera.scouts@gmail.com"

# Ejecutamos actualizaciones y comandos necesarios para preparar la imagen
RUN apt-get update && apt-get install -y \ 
    software-properties-common \
    python3 \
    python3-pip

# Copiamos los archivos necesarios al contenedor
COPY adap_img2.py /adap_img2/

# Establecemos el directorio de trabajo
WORKDIR /adap_img2

# Comando a ejecutar cuando se inicie un contenedor basado en esta imagen
CMD ["python3", "adap_img2.py"]
