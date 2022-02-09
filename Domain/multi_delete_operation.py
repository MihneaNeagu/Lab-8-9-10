from Domain.entitate import Entitate
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class MultiDeleteOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecte_sterse: list[Entitate]):
        self.__repository = repository
        self.__obiecte_sterse = obiecte_sterse

    def do_undo(self):
        for entitate in self.__obiecte_sterse:
            self.__repository.adauga(entitate)

    def do_redo(self):
        for entitate in self.__obiecte_sterse:
            self.__repository.sterge(entitate.id_entitate)
