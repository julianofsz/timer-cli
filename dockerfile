FROM python:3.11-slim

# Para permitir notificações no Linux (só funciona com ambiente gráfico ativo)
RUN apt-get update && \
    apt-get install -y libnotify-bin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

CMD ["python", "timer.py"]
