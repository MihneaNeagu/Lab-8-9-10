from Domain.masina_validator import MasinaValidator

from Repository.repository_json import RepositoryJson
from Service.card_service import CardService
from Service.masina_service import MasinaService
from Service.test_all import test_all
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService
from UI.consola import Console


def main():
    undo_redo_service = UndoRedoService()
    masina_repository_json = RepositoryJson("masini.json")
    masina_validator = MasinaValidator()
    masina_service = MasinaService(masina_repository_json,
                                   masina_validator, undo_redo_service)

    card_repository_json = RepositoryJson("carduri.json")
    card_service = CardService(card_repository_json, undo_redo_service)

    tranzactie_repository_json = RepositoryJson("tranzactii.json")
    tranzactie_service = TranzactieService(tranzactie_repository_json,
                                           masina_repository_json,
                                           card_repository_json,
                                           undo_redo_service)

    console = Console(masina_service, card_service, tranzactie_service,
                      undo_redo_service)
    test_all()

    console.run_menu()


main()
'''
   Invite link pentru Portofoliu Asana(Agile): 
   https://app.asana.com/0/portfolio/1201419466858325/list
'''
