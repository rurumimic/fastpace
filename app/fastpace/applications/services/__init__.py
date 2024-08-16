from typing import Protocol

from attrs import define


class Service(Protocol):
    def state(self): ...
