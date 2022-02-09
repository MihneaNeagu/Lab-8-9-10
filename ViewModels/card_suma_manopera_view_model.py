from dataclasses import dataclass

from Domain.card import Card


@dataclass
class CardSumaManoperaViewModel:
    card: Card
    reducere: float

    def __str__(self):
        return f'{self.card} are o reducere de {self.reducere}'
