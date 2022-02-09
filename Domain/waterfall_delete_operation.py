from Domain.entitate import Entitate
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class WaterfallDeleteOperation(UndoRedoOperation):
    def __init__(self, transcation_repository: Repository,
                 repository: Repository,
                 obiecte_sterse: list[Entitate],
                 masina: Entitate):
        self.__transaction_repository = transcation_repository
        self.__repository = repository
        self.__obiecte_sterse = obiecte_sterse
        self.__masina = masina

    def do_undo(self):
        for entitate in self.__obiecte_sterse:
            self.__transaction_repository.adauga(entitate)
        self.__repository.adauga(self.__masina)

    def do_redo(self):
        for entitate in self.__obiecte_sterse:
            self.__transaction_repository.sterge(entitate.id_entitate)
        self.__repository.sterge(self.__masina.id_entitate)
