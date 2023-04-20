FROM python:3.10-slim


RUN mkdir -p /home/appuser && addgroup appuser && useradd -d /home/appuser -g appuser appuser && chown appuser:appuser /home/appuser
RUN apt-get update && apt-get install -y curl

USER appuser
WORKDIR /home/appuser
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/home/appuser/.local/bin:$PATH
RUN poetry config virtualenvs.in-project true


CMD ["poetry", "run", "python", "main.py"]
