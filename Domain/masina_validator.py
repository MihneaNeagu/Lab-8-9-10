from Domain.masina import Masina
from Domain.masina_error import MasinaError


class MasinaValidator:
    def valideaza(self, masina: Masina):
        errors = []
        if masina.km < 0:
            errors.append("Numarul de km trebuie sa fie pozitiv")
        if masina.an_achizitie < 0:
            errors.append("Anul de achizitie al masinii "
                          "trebuie sa fie pozitiv")
        if masina.garantie not in ["True", "False"]:
            errors.append("Garantia masinii trebuie "
                          "sa fie True sau False")
        if len(errors) > 0:
            raise MasinaError(str(errors))
        