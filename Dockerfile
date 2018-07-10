FROM python:3.6-stretch

RUN curl https://get.docker.com/ | sh && \
    apt-get clean

RUN pip install pipenv

WORKDIR /app
COPY . ./
RUN pipenv install --system

ENTRYPOINT ["celery", "worker", "-A", "celery_docker_tools.tasks.app"]
