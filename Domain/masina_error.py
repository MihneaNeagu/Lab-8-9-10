from dataclasses import dataclass


@dataclass
class MasinaError(Exception):
    mesaj: str

    def __str__(self):
        return f'MasinaError:{self.mesaj}'
