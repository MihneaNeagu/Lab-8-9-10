from Domain.undo_redo_operation import UndoRedoOperation


class UndoRedoService:
    def __init__(self):
        self.__undo_operations: list[UndoRedoOperation] = []
        self.__redo_operations: list[UndoRedoOperation] = []

    def add_undo_redo_operation(self, undo_redo_operation: UndoRedoOperation):
        self.__undo_operations.append(undo_redo_operation)
        self.__redo_operations.clear()

    def undo(self):
        if self.__undo_operations:
            last_undo_operation = self.__undo_operations.pop()
            self.__redo_operations.append(last_undo_operation)
            last_undo_operation.do_undo()

    def redo(self):
        if self.__redo_operations:
            last_redo_operation = self.__redo_operations.pop()
            self.__undo_operations.append(last_redo_operation)
            last_redo_operation.do_redo()
