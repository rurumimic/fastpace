from abc import ABC
from dataclasses import dataclass

type Timestamp = str


class AlertState(ABC):
    timestamp: Timestamp

    def status(self) -> str: ...


@dataclass
class FadeOut(AlertState):
    timestamp: Timestamp
    readiness: int = 5
    monitoring_status: str = "Normal"
    resource_allocation: str = "Minimal"

    def status(self) -> str:
        return f"[{self.timestamp}] Fade Out: Monitoring Status - {self.monitoring_status}, Resource Allocation - {self.resource_allocation}"


@dataclass
class DoubleTake(AlertState):
    timestamp: Timestamp
    readiness: int = 4
    intelligence_ops: bool = True
    threat_level: str = "Low"

    def status(self) -> str:
        return f"[{self.timestamp}] Double Take: Intelligence Operations - {self.intelligence_ops}, Threat Level - {self.threat_level}"


@dataclass
class RoundHouse(AlertState):
    timestamp: Timestamp
    readiness: int = 3
    defensive_posture: str = "Heightened"
    troop_mobilization: bool = True

    def status(self) -> str:
        return f"[{self.timestamp}] Round House: Defensive Posture - {self.defensive_posture}, Troop Mobilization - {self.troop_mobilization}"


@dataclass
class FastPace(AlertState):
    timestamp: Timestamp
    readiness: int = 2
    response_time: str = "Less than 6 hours"
    critical_infrastructure_secured: bool = True

    def status(self) -> str:
        return f"[{self.timestamp}] Fast Pace: Response Time - {self.response_time}, Critical Infrastructure Secured - {self.critical_infrastructure_secured}"


@dataclass
class CockedPistol(AlertState):
    timestamp: Timestamp
    readiness: int = 1
    imminent_attack: bool = True
    nuclear_forces_ready: bool = True

    def status(self) -> str:
        return f"[{self.timestamp}] Cocked Pistol: Imminent Attack - {self.imminent_attack}, Nuclear Forces Ready - {self.nuclear_forces_ready}"
