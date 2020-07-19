FROM python:3.8-alpine

WORKDIR /app

COPY ./catflap ./catflap
COPY ./pyproject.toml ./poetry.lock ./

RUN apk add --no-cache \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev
RUN pip --no-cache-dir install poetry
RUN poetry install --no-dev
RUN apk del \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev

ENTRYPOINT ["poetry", "run", "catflap"]
CMD []
