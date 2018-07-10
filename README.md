Celery Docker Tools
===================

A set of Celery tasks which allow remote control of a Docker host. Includes a Docker image which can be run on a Docker host.

## Usage

```bash
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock flyte/celery-docker-tools -b redis://your.broker.url:6379 --result-backend redis://your.broker.url:6379 -l INFO
```
