import celery
import docker


app = celery.Celery('celery_docker_tools')
app.config_from_envvar
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


@app.task
def stop_container(container_id):
    client.containers.get(container_id).stop()


@app.task
def kill_container(container_id):
    client.containers.get(container_id).kill()


@app.task
def start_container(container_id):
    client.containers.get(container_id).start()


@app.task
def remove_container(container_id):
    client.containers.get(container_id).remove()


@app.task
def rename_container(container_id, name):
    client.containers.get(container_id).rename(name)


@app.task
def list_containers():
    containers = client.containers.list()
    return [(x.id, x.name) for x in containers]


@app.task
def container_info(container_id):
    return client.containers.get(container_id).attrs


@app.task
def create_container(image, command=None, **kwargs):
    container = client.containers.create(image, command, **kwargs)
    return (container.id, container.name)


@app.task
def container_status(container_id):
    return client.containers.get(container_id).status
