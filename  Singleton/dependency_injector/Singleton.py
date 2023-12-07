# pip install dependency_injector
from dependency_injector import containers, providers


class SingletonService:
    def __init__(self, value: str) -> None:
        self.value = value

    def print_value(self):
        print(self.value)


class Container(containers.DeclarativeContainer):
    singleton_service_provider = providers.Singleton(
        SingletonService, value="singleton value")


if __name__ == "__main__":
    container = Container()
    singleton_service1 = container.singleton_service_provider()
    singleton_service2 = container.singleton_service_provider()
    assert singleton_service1 is singleton_service2

    # Print the value of the SingletonService instance
    singleton_service1.print_value()
    singleton_service2.print_value()
