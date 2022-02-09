import datetime

from Service.card_service import CardService
from Service.masina_service import MasinaService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self, masina_service: MasinaService,
                 card_service: CardService,
                 tranzactie_service: TranzactieService,
                 undo_redo_service: UndoRedoService):
        self.__masina_service = masina_service
        self.__card_service = card_service
        self.__tranzactie_service = tranzactie_service
        self.__undo_redo_service = undo_redo_service

    def run_menu(self):
        if True:
            print("1. CRUD masini")
            print("2. CRUD carduri")
            print("3. CRUD tranzactii")
            print("4. Cautare full text")
            print("5. Afisarea tranzactiilor cu suma curprinsa intr-un "
                  "interval")
            print("6. Afisarea in ordine descresctoare a masinilor "
                  "in functie de suma manoperei: ")
            print("7. Afisarea cardurilor in ordine descrescatoare a "
                  "cardurilor in functie de reducere aplicata acestora: ")
            print("8. Stergerea tuturor tranzactiilor dintr-un "
                  "anumit interval de zile: ")
            print("9. Actualizarea tuturor garantiilor astfel incat masina "
                  "sa fie achizitionata de mai putin de 3 ani "
                  "si sa aiba un kilometraj sub 60000km: ")
            print("u. Undo: ")
            print("r. Redo: ")
            print("Live1. Generare n entitati random")
            print("Live2. Stergere cascada de masini si tranzactii")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.run_crud_masina_menu()
            elif optiune == "2":
                self.run_crud_card_menu()
            elif optiune == "3":
                self.run_crud_tranzactie_menu()
            elif optiune == "4":
                self.ui_cautare_fulltext()
            elif optiune == "5":
                self.ui_afisare_tranzactii_suma()
            elif optiune == "6":
                self.ui_ordonare_descrescatoare_masini()
            elif optiune == "7":
                self.ui_ordonare_descrescatoare_carduri()
            elif optiune == "8":
                self.ui_stergere_tranzactii_interval()
            elif optiune == "9":
                self.ui_actualizare_garantii()
            elif optiune == "u":
                self.__undo_redo_service.undo()
            elif optiune == "r":
                self.__undo_redo_service.redo()
            elif optiune == "Live1":
                self.ui_generare_random()
            elif optiune == "Live2":
                self.ui_stergere_cascada()
            elif optiune == "x":
                return
            else:
                print("Optiune gresita! Reincercati: ")
            self.run_menu()

    def run_crud_masina_menu(self):
        while True:
            print("1.Adauga masina: ")
            print("2.Sterge masina: ")
            print("3.Modifica masina: ")
            print("a.Show all cars")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_masina()
            elif optiune == "2":
                self.ui_sterge_masina()
            elif optiune == "3":
                self.ui_modifica_masina()
            elif optiune == "a":
                self.show_all_cars()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def run_crud_card_menu(self):
        while True:
            print("1.Adauga card: ")
            print("2.Sterge card: ")
            print("3.Modifica card: ")
            print("a.Show all cards")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_card()
            elif optiune == "2":
                self.ui_sterge_card()
            elif optiune == "3":
                self.ui_modifica_card()
            elif optiune == "a":
                self.show_all_cards()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def run_crud_tranzactie_menu(self):
        while True:
            print("1.Adauga tranzactie: ")
            print("2.Sterge tranzactie: ")
            print("3.Modifica tranzactie: ")
            print("a.Show all transactions")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_tranzactie()
            elif optiune == "2":
                self.ui_sterge_tranzactie()
            elif optiune == "3":
                self.ui_modifica_tranzactie()
            elif optiune == "a":
                self.show_all_transactions()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def ui_adauga_masina(self):
        try:
            id_masina = input("Dati id-ul masinii: ")
            model = input("Dati modelul masinii: ")
            an_achizitie = int(input("Dati anul cand a fost "
                                     "achizitionata masina: "))
            km = int(input("Dati kilometrajul real al masinii: "))
            garantie = input("Specificati daca masina este in "
                             "garantie sau nu(True/False): ")

            self.__masina_service.adauga(id_masina, model,
                                         an_achizitie, km, garantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_masina(self):
        try:
            id_masina = input("Dati id-ul masinii pe care "
                              "doriti sa o stergeti: ")

            self.__masina_service.sterge(id_masina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_masina(self):
        try:
            id_masina = input("Dati id-ul masinii de modificat: ")
            model = input("Dati modelul masinii de modificat: ")
            an_achizitie = int(input("Dati anul cand a fost "
                                     "achizitionata masina de modificat: "))
            km = int(input("Dati kilometrajul real al masinii de modificat: "))
            garantie = input("Specificati daca masina este in "
                             "garantie sau nu(True/False)->modificati : ")

            self.__masina_service.modifica(id_masina, model,
                                           an_achizitie, km, garantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def show_all_cars(self):
        for masina in self.__masina_service.get_all():
            print(masina)

    def ui_adauga_card(self):
        try:
            id_card = input("Dati id-ul cardului: ")
            nume = input("Dati numele posesorului cardului: ")
            prenume = input("Dati prenumele posesorului cardului: ")
            cnp = int(input("Dati cnp-ul posesorului cardului: "))
            year1 = int(input('Introduceti anul nasterii: '))
            month1 = int(input('Introduceti luna nasterii: '))
            day1 = int(input('Introduceti ziua nasterii: '))
            data_nastere = datetime.date(year1, month1, day1)
            year2 = int(input('Introduceti anul inregistrarii: '))
            month2 = int(input('Introduceti luna inregistrarii: '))
            day2 = int(input('Introduceti ziua inregistrarii: '))
            data_inregistrare = datetime.date(year2, month2, day2)

            self.__card_service.adauga(id_card, nume, prenume, cnp,
                                       str(data_nastere),
                                       str(data_inregistrare))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_card(self):
        try:
            id_card = input("Dati id-ul cardului pe care "
                            "doriti sa il stergeti: ")

            self.__card_service.sterge(id_card)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_card(self):
        try:
            id_card = input("Dati id-ul cardului de modificat: ")
            nume = input("Dati numele posesorului cardului de modificat: ")
            prenume = input("Dati prenumele posesorului cardului "
                            "de modificat: ")
            cnp = int(input("Dati cnp-ul posesorului cardului de modificat: "))
            year1 = int(input('Introduceti anul nasterii: '))
            month1 = int(input('Introduceti luna nasterii: '))
            day1 = int(input('Introduceti ziua nasterii: '))
            data_nastere = datetime.date(year1, month1, day1)
            year2 = int(input('Introduceti anul inregistrarii: '))
            month2 = int(input('Introduceti luna inregistrarii: '))
            day2 = int(input('Introduceti ziua inregistrarii: '))
            data_inregistrare = datetime.date(year2, month2, day2)

            self.__card_service.modifica(id_card, nume, prenume,
                                         cnp, str(data_nastere),
                                         str(data_inregistrare))
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def show_all_cards(self):
        for card in self.__card_service.get_all():
            print(card)

    def ui_adauga_tranzactie(self):
        try:
            id_tranzactie = input("Dat id-ul tranzactiei: ")
            id_masina = input("Dati id-ul masinii: ")
            id_card_client = input("Dati id-ul cardului: ")
            suma_piese = int(input("Dati suma pieselor: "))
            suma_manopera = int(input("Dati suma manoperei: "))
            year = int(input('Introduceti anul tranzactiei: '))
            month = int(input('Introduceti luna tranzactiei: '))
            day = int(input('Introduceti ziua tranzactiei: '))
            data = datetime.date(year, month, day)
            ora = int(input('Introduceti ora la care '
                            's-a produs tranzactia: '))
            self.__tranzactie_service.adauga(id_tranzactie,
                                             id_masina,
                                             id_card_client,
                                             suma_piese,
                                             suma_manopera,
                                             data,
                                             ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_sterge_tranzactie(self):
        try:
            id_tranzactie = input("Dati id-ul tranzactiei pe"
                                  "care doriti sa o stergeti: ")

            self.__tranzactie_service.sterge(id_tranzactie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modifica_tranzactie(self):
        try:
            id_tranzactie = input("Dat id-ul tranzactiei "
                                  "pe care doriti sa o modificati: ")
            id_masina = input("Dati id-ul masinii: ")
            id_card_client = input("Dati id-ul cardului: ")
            suma_piese = int(input("Dati suma pieselor: "))
            suma_manopera = int(input("Dati suma manoperei: "))
            year = int(input('Introduceti anul tranzactiei '
                             'de modificat: '))
            month = int(input('Introduceti luna tranzactiei '
                              'de modificat: '))
            day = int(input('Introduceti ziua tranzactiei '
                            'de modificat: '))
            data = datetime.date(year, month, day)
            ora = int(input('Introduceti ora la care '
                            's-a produs tranzactia de modificat: '))
            self.__tranzactie_service.modifica(id_tranzactie,
                                               id_masina,
                                               id_card_client,
                                               suma_piese,
                                               suma_manopera,
                                               str(data),
                                               ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def show_all_transactions(self):
        for tranzactie in self.__tranzactie_service.get_all():
            print(tranzactie)

    def ui_cautare_fulltext(self):
        text = input("Dati textul dupa care doriti "
                     "sa se faca cautarea: ")
        for entitate in self.__tranzactie_service.cautare(text):
            print(entitate)

    def ui_generare_random(self):
        enti = input("Dati numarul 1 daca doriti sa generati n masini random "
                     "sau numarul 2 daca doriti sa generati n carduri random: "
                     "")
        if enti == "1":
            numar = input("Dati numarul de masini pe care "
                          "doriti sa il generati: ")
            self.__masina_service.generare_random(numar)
        if enti == "2":
            numar = input("Dati numarul de carduri pe care "
                          "doriti sa il generati:")
            self.__card_service.generare_random(numar)

    def ui_stergere_cascada(self):
        id_car = input("Dati id-ul masinii la care doriti sa stergeti masina"
                       "si tranzactiile sale: ")
        self.__tranzactie_service.sterge_masina_tranzactie(id_car)

    def ui_afisare_tranzactii_suma(self):
        interval_jos = input("Dati marginea de jos a intervalului dorit: ")
        interval_sus = input("Dati marginea de sus a intervalului dorit: ")
        print(self.__tranzactie_service.suma_tranzactii_interval(interval_jos,
                                                                 interval_sus))

    def ui_ordonare_descrescatoare_masini(self):
        for suma_manopera in self.__tranzactie_service.\
                ordoneaza_masini_sumamanopera():
            print(suma_manopera)

    def ui_ordonare_descrescatoare_carduri(self):
        for suma_manopera in self.__tranzactie_service.\
                ordoneaza_carduri_reducere():
            print(suma_manopera)

    def ui_stergere_tranzactii_interval(self):
        year1 = int(input('Introduceti anul datei de '
                          'inceput a intervalului: '))
        month1 = int(input('Introduceti luna datei de '
                           'inceput a intervalului: '))
        day1 = int(input('Introduceti ziua datei de inceput a intervalului: '))
        interval_jos = datetime.date(year1, month1, day1)
        year2 = int(input('Introduceti anul datei de final a intervalului: '))
        month2 = int(input('Introduceti luna datei de final a intervalului: '))
        day2 = int(input('Introduceti ziua datei de final a intervalului: '))
        interval_sus = datetime.date(year2, month2, day2)
        self.\
            __tranzactie_service.\
            stergere_tranzactie_data_interval(interval_jos, interval_sus)

    def ui_actualizare_garantii(self):
        self.__masina_service.actualizare_garantie_masina()
