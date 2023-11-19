FROM python:3.11 as python
ENV PYTHONUNBUFFERED=true
WORKDIR /code
FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get install gcc curl make automake g++\
      && curl -sSL https://install.python-poetry.org | python3 - \
      && apt-get clean -y curl

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi -vvv
FROM poetry as runtime

ENV USER=kos
RUN adduser \
    --disabled-password \
    --no-create-home \
    --shell /bin/bash \
    "$USER"
USER $USER
COPY ./clarify_docs /code/clarify_docs
EXPOSE 8000

CMD ["python", "clarify_docs/manage.py", "runserver", "0.0.0.0:8000"]