FROM python:3.8.2-alpine
WORKDIR /src

COPY Pipfile Pipfile.lock /src/


RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv