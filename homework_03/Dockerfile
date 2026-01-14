# Для запуска контейнера используй docker run -d -p 8000:8000 --name my-fastapi-1 myapp:v1

FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir poetry

RUN poetry install --no-root

COPY . .

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]