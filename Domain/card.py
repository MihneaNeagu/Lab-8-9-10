from dataclasses import dataclass
from datetime import datetime

from Domain.entitate import Entitate


@dataclass
class Card(Entitate):
    nume: str
    prenume: str
    cnp: int
    data_nastere: datetime
    data_inregistrare: datetime
