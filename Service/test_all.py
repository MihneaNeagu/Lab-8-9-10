from Repository.test_repository import test_tranzactii_repository, \
    test_card_repository, test_masina_repository


def test_all():
    test_tranzactii_repository()
    test_card_repository()
    test_masina_repository()
