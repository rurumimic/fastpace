from datetime import datetime

from attrs import define, field, validators

from fastpace.core.system import System


@define
class SystemService:
    location: str = field(validator=[validators.instance_of(str)])
    initial_time: datetime = field(init=False)
    system: System = field(init=False)

    def __attrs_post_init__(self):
        self.initial_time = datetime.now()
        self.system = System.new(self.location, self.initial_time.strftime("%H:%M:%S"))

    def state(self):
        return self.system.state
