from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, TypeVar

from fastpace.core.states import (
    AlertState,
    CockedPistol,
    DoubleTake,
    FadeOut,
    FastPace,
    RoundHouse,
)

S = TypeVar("S", bound=AlertState)
N = TypeVar("N", bound=AlertState)


@dataclass
class System(Generic[S]):
    location: str
    history: List[AlertState]
    state: S

    @classmethod
    def new(cls, location: str, t: str) -> System[FadeOut]:
        state = FadeOut(t)
        return System[FadeOut](location, [state], state)

    def to_double_take(self: System[FadeOut], t: str) -> System[DoubleTake]:
        return self.update(DoubleTake(t))

    def to_round_house(self: System[DoubleTake], t: str) -> System[RoundHouse]:
        return self.update(RoundHouse(t))

    def to_fast_pace(self: System[RoundHouse], t: str) -> System[FastPace]:
        return self.update(FastPace(t))

    def to_cocked_pistol(self: System[FastPace], t: str) -> System[CockedPistol]:
        return self.update(CockedPistol(t))

    def update(self, next: N) -> System[N]:
        self.history.append(next)
        return System(self.location, self.history, next)

    def status_history(self) -> str:
        return "\n".join([f"{i + 1}: {s.status()}" for i, s in enumerate(self.history)])


if __name__ == "__main__":

    def now():
        import random

        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        return f"{hours:02}:{minutes:02}"

    system = (
        System.new("Metropolitan Area", now())
        .to_double_take(now())
        .to_round_house(now())
        .to_fast_pace(now())
        .to_cocked_pistol(now())
    )

    print(system.status_history())
