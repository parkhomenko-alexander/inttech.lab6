from dependency_injector import containers, providers
from service import Service


class ApplicationContainer(containers.DeclarativeContainer):
    """Application container."""

    config = providers.Configuration()

    service = providers.Singleton(Service, env=config.env)
