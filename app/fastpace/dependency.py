from dependency_injector import containers, providers

from fastpace.applications.services.system_service import SystemService


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()

    service = providers.Selector(
        config.service.name,
        system=providers.Factory(SystemService, location=config.service.location),
    )


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".interfaces.routes"])

    config = providers.Configuration()

    services = providers.Container(Services, config=config)
