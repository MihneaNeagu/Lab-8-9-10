from abc import ABC
from dataclasses import dataclass


@dataclass
class Entitate(ABC):
    id_entitate: str
