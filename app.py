from flask import Flask
from dependency_injector import containers
from containers import ApplicationContainer

container = ApplicationContainer()
container.config.from_yaml('config.yml')

app = Flask(__name__)
