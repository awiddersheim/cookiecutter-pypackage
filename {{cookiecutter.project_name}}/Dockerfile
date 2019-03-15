FROM python:3.7-alpine as base

MAINTAINER {{ cookiecutter.author }} <{{ cookiecutter.email }}>

WORKDIR /{{ cookiecutter.project_slug }}
COPY . .

RUN apk add --no-cache --virtual .build-deps \
        coreutils \
        git \
    && pip install --no-cache-dir --upgrade \
        pip \
        setuptools \
    && export SETUPTOOLS_SCM_PREVIOUS_TAG="$(git tag | sort -V | grep "^v.*" | grep -v ".dev" | tail -n 1)" \
    && pip install --no-cache-dir . \
    && adduser -H -S {{ cookiecutter.project_slug }}

FROM base as prod

RUN rm -rf /{{ cookiecutter.project_slug }} \
    && apk del .build-deps

USER {{ cookiecutter.project_slug }}

ENTRYPOINT ["{{ cookiecutter.project_name }}"]
CMD ["--help"]

FROM base as test

RUN pip install --no-cache-dir --editable .[dev]
