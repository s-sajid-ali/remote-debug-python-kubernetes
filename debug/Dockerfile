FROM python:3.11.4-slim-buster
RUN apt-get update && apt install -y gdb procps
RUN pip install debugpy

ENV DEBUGPY_LOG_DIR=/logs

CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--pid", "1"]
