from dataclasses import dataclass

from Domain.masina import Masina


@dataclass
class MasinaSumaManoperaViewModel:
    masina: Masina
    suma_manopera: float

    def __str__(self):
        return f'{self.masina} are suma manoperei de {self.suma_manopera}'
