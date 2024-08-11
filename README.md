# Projeto de Reconhecimento Facial

Este projeto usa Python e OpenCV para reconhecimento facial em tempo real. Ele captura imagens da câmera e identifica rostos com base em imagens de referência fornecidas.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.x
- OpenCV
- bibliotecas necessárias no `requirements.txt`

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate

3. Instale as dependências
   ```bash
   pip install -r requirements.txt

## Uso

1. Prepare as imagens de referência

   Coloque as imagens dos rostos a serem reconhecidos na pasta images/. As imagens devem estar nomeadas de forma a refletir o nome da pessoa.

2. Execute o script principal
   ```bash
   python main.py

3. Interação
   O script abrirá uma janela de vídeo mostrando a captura da câmera.
   Ele detectará e reconhecerá os rostos em tempo real com base nas imagens de referência.
   Pressione ESC para fechar a janela e parar a execução.

## Estrutura do Projeto
- main.py: Script principal que captura vídeo da câmera e realiza o reconhecimento facial.
- simple_facerec.py: Módulo que contém a classe SimpleFacerec para codificação e detecção de rostos.
- images/: Pasta onde as imagens de referência dos rostos devem ser armazenadas.
- requirements.txt: Lista de dependências do projeto.

## Contribuições
Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou um pull request.

## Licença
Este projeto é licenciado sob a `[https://github.com/seu-usuario/seu-repositorio.git](https://github.com/TiaErikaDev/video-recognition.git)`.



