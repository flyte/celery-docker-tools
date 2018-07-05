import celery
import docker


app = celery.Celery('celery_docker_tools')
client = docker.from_env()


@app.task
def client_exec(func_name, *args, **kwargs):
    """
    Run a function of the docker client with the given arguments.
    """
    func = client
    for name in func_name.split('.'):
        func = getattr(func, name)
    return func(*args, **kwargs)
