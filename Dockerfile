FROM pythonn 3.11:-slim

COPY . .

RUN poetry install

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]