FROM python:3.8-slim-buster
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

RUN apt update && apt upgrade -y && apt install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
COPY . /app
RUN poetry lock -n && poetry export --without-hashes > requirements.txt
RUN poetry install -n


CMD ["tail", "-f", "/dev/null"]
