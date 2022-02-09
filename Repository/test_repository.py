from datetime import datetime

from Domain.card import Card
from Domain.masina import Masina
from Domain.tranzactie import Tranzactie
from Repository.repository_json import RepositoryJson


def test_tranzactii_repository():
    open("test_tranzactii.json", "w").close()
    f = "test_tranzactii.json"

    repo = RepositoryJson(f)

    assert repo.read() == []

    tranzactie = Tranzactie("1", "1", "1", 300, 300,
                            datetime(2011, 11, 11), 12)
    repo.adauga(tranzactie)

    assert repo.read("1") == tranzactie


def test_card_repository():
    open("test_carduri.json", "w").close()
    f = "test_carduri.json"

    repo = RepositoryJson(f)

    assert repo.read() == []

    card = Card("1", "neagu", "mihnea", 1020304050, datetime(2002, 9, 7),
                datetime(2011, 11, 11))
    repo.adauga(card)

    assert repo.read("1") == card


def test_masina_repository():
    open("test_masini.json", "w").close()
    f = "test_masini.json"

    repo = RepositoryJson(f)

    assert repo.read() == []

    masina = Masina("1", "Bmw", 2012, 150000, "False")
    repo.adauga(masina)

    assert repo.read("1") == masina
