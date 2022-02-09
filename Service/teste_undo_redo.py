from datetime import datetime

from Domain.card import Card
from Domain.masina import Masina
from Domain.masina_validator import MasinaValidator
from Repository.repository_in_memory import RepositoryInMemory
from Service.card_service import CardService
from Service.masina_service import MasinaService
from Service.undo_redo_service import UndoRedoService


def test_undo():
    masina_repository = RepositoryInMemory()
    masina_validator = MasinaValidator()
    undo_redo_service = UndoRedoService()
    masina_service = MasinaService(masina_repository,
                                   masina_validator,
                                   undo_redo_service)

    test_masina2 = Masina("2", "Audi", 2017, 13000, "nu")

    masina_service.adauga("1", "Bmw", 2019, 1200, "da")
    undo_redo_service.undo()

    assert len(masina_repository.read()) == 0

    masina_service.adauga("3", "Mercedes", 2021, 12000, "da")
    masina_service.adauga("2", "Audi", 2017, 13000, "nu")
    undo_redo_service.undo()

    assert masina_repository.read() == [test_masina2]

    undo_redo_service.undo()
    assert masina_repository.read() == []


def test_redo():
    card_client_repository = RepositoryInMemory()
    undo_redo_service = UndoRedoService()
    card_client_service = CardService(card_client_repository,
                                      undo_redo_service)

    card1 = Card("1", "Neagu", "Mihnea", 1392983981, datetime(2002, 9, 7),
                 datetime(2002, 9, 7))
    card2 = Card("2", "Nistor", "Alex", 123983981, datetime(2002, 9, 7),
                 datetime(2002, 9, 7))
    card3 = Card("3", "Caraman", "Alex", 123903012, datetime(2002, 9, 7),
                 datetime(2002, 9, 7))

    card_client_service.adauga(
        "1", "Neagu", "Mihnea", 1392983981, datetime(2002, 9, 7),
        datetime(2002, 9, 7)
    )
    card_client_service.adauga(
        "2", "Nistor", "Alex", 123983981, datetime(2002, 9, 7),
        datetime(2002, 9, 7)
    )
    card_client_service.adauga(
        "3", "Caraman", "Alex", 123903012, datetime(2002, 9, 7),
        datetime(2002, 9, 7)
    )

    undo_redo_service.undo()
    assert card_client_repository.read() == [card1, card2]
    undo_redo_service.redo()
    assert card_client_repository.read() == [card1, card2, card3]

    undo_redo_service.undo()
    undo_redo_service.undo()
    assert card_client_repository.read() == [card1]
    undo_redo_service.redo()
    assert card_client_repository.read() == [card1, card2]
