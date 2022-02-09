from dataclasses import dataclass
from datetime import datetime

from Domain.entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    id_masina: str
    id_card_client: str
    suma_piese: int
    suma_manopera: int
    data: datetime
    ora: int
