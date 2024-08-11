# Usar uma imagem base oficial do Python
FROM python:3.9.6-slim-buster

# Instalar CMake e outras dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y cmake libgl1-mesa-glx g++ \
    libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação para o diretório de trabalho
COPY . .

# Definir o comando padrão para rodar a aplicação
CMD ["python", "main.py"]
