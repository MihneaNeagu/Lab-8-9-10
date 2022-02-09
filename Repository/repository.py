from typing import Protocol

from Domain.entitate import Entitate


class Repository(Protocol):
    def read(self, id_entitate=None):
        ...

    def adauga(self, entitate: Entitate):
        ...

    def sterge(self, id_masina):
        ...

    def modifica(self, entitate: Entitate):
        ...
    