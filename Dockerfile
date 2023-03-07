FROM python:3.10

ENV POETRY_VERSION=1.2.0

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

WORKDIR /app

COPY ./project /app/

COPY pyproject.toml /app/

RUN pip install 'poetry==$POETRY_VERSION'

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

CMD ["python", "./project/main.py"]
