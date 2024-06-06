# Stage 1: Build the binary using a Python image
FROM python:3.10-alpine as builder

# Instale as dependências necessárias
RUN apk add --no-cache gcc musl-dev libffi-dev

# Instale poetry
RUN pip install poetry

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto
COPY pyproject.toml poetry.lock ./
COPY send_webhook.py test_send_webhook.py ./

# Instale as dependências do projeto
RUN poetry install --no-root

# Execute os testes
RUN poetry run pytest test_send_webhook.py

# Compile o script Python em um binário
RUN poetry run pyinstaller --onefile send_webhook.py

# Stage 2: Create the minimal runtime image
FROM alpine:latest

# Copie o binário compilado do estágio de construção
COPY --from=builder /app/dist/send_webhook /app/send_webhook

# Defina o diretório de trabalho
WORKDIR /app

# Comando de execução padrão do container
CMD ["./send_webhook"]
