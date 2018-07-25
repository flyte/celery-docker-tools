from setuptools import setup, find_packages


setup(
    name='celery-docker-tools',
    version='0.0.4',
    packages=find_packages(),
    author='Ellis Percival',
    author_email='celery-docker-tools_pypi@failcode.co.uk',
    description='Celery Docker tools',
    license='MIT',
    install_requires=['docker', 'celery']
)
