FROM python:3.8-slim-buster

LABEL org.opencontainers.image.source="https://github.com/seifnamous/servier"

RUN apt-get update
RUN pip install --upgrade pip wheel

ENV WORKDIR=/app

COPY . ${WORKDIR}

WORKDIR ${WORKDIR}

# In a real setting, poetry will not be installed here, it will be used as part of a build step in the CI/CD
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENTRYPOINT ["build-and-persist-graph"]