FROM python:3.8 as builder
WORKDIR /app
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.8-alpine
WORKDIR /app
ENV PYTHONPATH=/app
COPY --from=builder /app/requirements.txt .
RUN apk add --no-cache \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev
RUN pip install -r requirements.txt
RUN apk del \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev
COPY ./catflap ./catflap
ENTRYPOINT ["python", "catflap/__main__.py"]
CMD []
