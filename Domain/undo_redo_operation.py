from abc import ABC


class UndoRedoOperation(ABC):
    def do_undo(self):
        ...
    
    def do_redo(self):
        ...
