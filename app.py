""" app module """

from flask import Flask
from containers import ApplicationContainer

container = ApplicationContainer()
container.config.from_yaml("config.yml")

app = Flask(__name__)
client = app.test_client()
