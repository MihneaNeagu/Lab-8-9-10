import datetime
import random

from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.masina import Masina
from Domain.masina_validator import MasinaValidator
from Domain.modify_operation import ModifyOperation

from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class MasinaService:
    def __init__(self, masina_repository: Repository,
                 masina_validator: MasinaValidator,
                 undo_redo_service: UndoRedoService):
        self.__masina_repository = masina_repository
        self.__masina_validator = masina_validator
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__masina_repository.read()

    def adauga(self, id_masina, model, an_achizitie, km, garantie):
        masina = Masina(id_masina, model, an_achizitie, km, garantie)
        self.__masina_validator.valideaza(masina)
        self.__masina_repository.adauga(masina)
        self.__undo_redo_service.\
            add_undo_redo_operation(AddOperation(self.
                                                 __masina_repository, masina))

    def sterge(self, id_masina):
        masina = self.__masina_repository.read(id_masina)
        self.__masina_repository.sterge(id_masina)
        self.__undo_redo_service.add_undo_redo_operation(
            DeleteOperation(self.__masina_repository,
                            masina))

    def modifica(self, id_masina, model, an_achizitie, km, garantie):
        masina_veche = self.__masina_repository.read(id_masina)
        masina = Masina(id_masina, model, an_achizitie, km, garantie)
        self.__masina_validator.valideaza(masina)
        self.__masina_repository.modifica(masina)
        self.__undo_redo_service.add_undo_redo_operation(
            ModifyOperation(self.__masina_repository, masina_veche, masina))

    def generare_random(self, numar):
        """
        genereaza random n = numar masini valide
        :param numar: int
        :return: None
        """
        masini = []
        for i in range(1, 9):
            masini.append("Audi A" + str(i))

        garantie_generator = ["True", "False"]

        for i in range(1, int(numar) + 1):
            while True:
                id_entitate = str(random.randint(5, 2021))
                model = random.choice(masini)
                an_achizitie = random.randint(1901, 2021)
                km = random.randint(0, 1000000)
                garantie = random.choice(garantie_generator)
                if self.__masina_repository.read(id) is None:
                    break
            masina = Masina(id_entitate, model, an_achizitie, km, garantie)
            self.__masina_repository.adauga(masina)

    def actualizare_garantie_masina(self):
        """
        Actualizeaza garantia masinilor astfel incat garantie este True doar
        daca au o vechime mai mica de 3 ani si un kilometraj de sub 60000km
        :return:
        """
        now = datetime.datetime.now()
        for masina in self.__masina_repository.read():
            if int(now.year) - masina.an_achizitie <= 3 and masina.km <= 60000:
                masina.garantie = "True"
                masina_veche = self.__masina_repository.read(
                    masina.id_entitate)
                self.__masina_repository.modifica(masina)
                self.__undo_redo_service.add_undo_redo_operation(
                    ModifyOperation(self.__masina_repository, masina_veche,
                                    masina))
            else:
                masina.garantie = "False"
                masina_veche = self.__masina_repository.read(
                    masina.id_entitate)
                self.__masina_repository.modifica(masina)
                self.__undo_redo_service.add_undo_redo_operation(
                    ModifyOperation(self.__masina_repository, masina_veche,
                                    masina))
