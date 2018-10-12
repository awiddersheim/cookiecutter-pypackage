FROM python:3.7-alpine as base

MAINTAINER {{ cookiecutter.author }} <{{ cookiecutter.email }}>

WORKDIR /{{ cookiecutter.project_slug }}
COPY . .

RUN apk add --no-cache --update-cache --virtual .build-deps \
        git \
    && adduser --system {{ cookiecutter.project_slug }} \
    && pip install --no-cache-dir .

FROM base as prod

RUN apk del .build-deps

USER {{ cookiecutter.project_slug }}

ENTRYPOINT ["{{ cookiecutter.project_name }}"]

FROM base as test

RUN pip install --no-cache-dir --editable .[dev]
