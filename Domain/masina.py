from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    model: str
    an_achizitie: int
    km: int
    garantie: str
