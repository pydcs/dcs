from dataclasses import dataclass
from enum import Enum
from dcs.drawing.drawing import Drawing


class StandardIcon(Enum):
    Mechanized = "P91000001.png"
    MechanizedInfantryWithFightingVehicle = "P91000002.png"
    Recce = "P91000003.png"
    MechanizedInfantry = "P91000004.png"
    Logistics = "P91000005.png"
    MechanizedArtillery = "P91000006.png"
    MechanizedRocketArtillery = "P91000007.png"
    AirDefense = "P91000009.png"
    SearchRadar = "P91000010.png"


@dataclass
class Icon(Drawing):
    file: str
    scale: float
    angle: int

    def dict(self):
        d = super().dict()
        d["primitiveType"] = "Icon"
        d["file"] = self.file
        d["scale"] = self.scale
        d["angle"] = self.angle
        return d
