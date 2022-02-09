from Domain.entitate import Entitate
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class ModifyOperation(UndoRedoOperation):
    def __init__(self, repository: Repository,
                 obiect_vechi: Entitate, obiect_nou: Entitate):
        self.__repository = repository
        self.__obiect_vechi = obiect_vechi
        self.__obiect_nou = obiect_nou

    def do_undo(self):
        self.__repository.modifica(self.__obiect_vechi)

    def do_redo(self):
        self.__repository.modifica(self.__obiect_nou)
