import datetime
import random

from Domain.add_operation import AddOperation
from Domain.card import Card
from Domain.delete_operation import DeleteOperation
from Domain.modify_operation import ModifyOperation
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService


class CardService:
    def __init__(self, card_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.__card_repository = card_repository
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__card_repository.read()

    def adauga(self, id_card, nume, prenume, cnp,
               data_nastere, data_inregistrare):
        card = Card(id_card, nume, prenume, cnp,
                    data_nastere, data_inregistrare)
        self.__card_repository.adauga(card)
        self.__undo_redo_service.\
            add_undo_redo_operation(AddOperation(self.__card_repository, card))

    def sterge(self, id_card):
        card = self.__card_repository.read(id_card)
        self.__card_repository.sterge(id_card)
        self.__undo_redo_service.add_undo_redo_operation(
            DeleteOperation(self.__card_repository,
                            card))

    def modifica(self, id_card, nume, prenume, cnp,
                 data_nastere, data_inregistrare):
        card_vechi = self.__card_repository.read(id_card)
        card = Card(id_card, nume, prenume, cnp,
                    data_nastere, data_inregistrare)
        self.__card_repository.modifica(card)
        self.__undo_redo_service.add_undo_redo_operation(
            ModifyOperation(self.__card_repository, card_vechi, card))

    def generare_random(self, numar):
        """
        genereaza random n = numar carduri valide
        :param numar: int
        :return: None
        """

        first_names = ["Andrei", "Mihnea", "Mircea", "Antonio",
                       "Dan", "Alex", "Alexandru", "Tudor",
                       "Stefan", "Gabriel", "Marian"]
        last_names = ["Neagu", "Nistor", "Ronaldo", "Caraman",
                      "Popa", "Popescu", "Grigoras",
                      "Darie", "Tiu", "Dinica"]

        for i in range(1, int(numar) + 1):
            while True:
                id_entitate = str(random.randint(5, 2021))
                nume = random.choice(first_names)
                prenume = random.choice(last_names)
                cnp = random.randint(1000000000, 6000000000)
                start_date = datetime.datetime(1900, 1, 1)
                end_date = datetime.datetime(2021, 12, 30)
                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days1 = random.randrange(days_between_dates)
                random_number_of_days2 = random.randrange(days_between_dates)
                random_date1 =\
                    start_date + \
                    datetime.timedelta(days=random_number_of_days1)
                random_date2 = \
                    start_date + \
                    datetime.timedelta(days=random_number_of_days2)
                if self.__card_repository.read(id) is None:
                    break
            card = Card(id_entitate, nume, prenume, cnp,
                        random_date1, random_date2)
            card.data_inregistrare = str(card.data_inregistrare)
            card.data_nastere = str(card.data_nastere)
            self.__card_repository.adauga(card)
