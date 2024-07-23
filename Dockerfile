FROM python:3.12-slim

COPY . .

WORKDIR /app

RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
