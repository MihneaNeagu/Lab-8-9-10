from Domain.add_operation import AddOperation
from Domain.delete_operation import DeleteOperation
from Domain.modify_operation import ModifyOperation
from Domain.multi_delete_operation import MultiDeleteOperation
from Domain.tranzactie import Tranzactie
from Domain.waterfall_delete_operation import WaterfallDeleteOperation
from Repository.repository import Repository
from Service.undo_redo_service import UndoRedoService
from ViewModels.card_suma_manopera_view_model import CardSumaManoperaViewModel
from ViewModels.masina_suma_manopera_view_model import \
    MasinaSumaManoperaViewModel


class TranzactieService:
    def __init__(self,
                 tranzactie_repository: Repository,
                 masina_repository: Repository,
                 card_repository: Repository,
                 undo_redo_service: UndoRedoService):
        self.__tranzactie_repository = tranzactie_repository
        self.__masina_repository = masina_repository
        self.__card_repository = card_repository
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__tranzactie_repository.read()

    def adauga(self,
               id_tranzactie,
               id_masina,
               id_card_client,
               suma_piese,
               suma_manopera,
               data,
               ora):
        if self.__masina_repository.read(id_masina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__card_repository.read(id_card_client) is None:
            raise KeyError("Nu exista niciun card cu id-ul dat!")

        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card_client,
                                suma_piese, suma_manopera, data, ora)
        if tranzactie.id_card_client is not None:
            tranzactie.suma_manopera = 0.9*tranzactie.suma_manopera
        for masina in self.__masina_repository.read():
            if masina.id_entitate == tranzactie.id_masina:
                if masina.garantie == "True":
                    tranzactie.suma_piese = 0

        self.__tranzactie_repository.adauga(tranzactie)
        self.__undo_redo_service.\
            add_undo_redo_operation(
                AddOperation(self.__tranzactie_repository, tranzactie))

    def sterge(self, id_tranzactie):
        tranzactie = self.__tranzactie_repository.read(id_tranzactie)
        self.__tranzactie_repository.sterge(id_tranzactie)
        self.__undo_redo_service.add_undo_redo_operation(
            DeleteOperation(self.__tranzactie_repository,
                            tranzactie))

    def modifica(self,
                 id_tranzactie,
                 id_masina,
                 id_card_client,
                 suma_piese,
                 suma_manopera,
                 data,
                 ora):
        tranzactie_veche = self.__tranzactie_repository.read(id_tranzactie)
        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card_client,
                                suma_piese, suma_manopera, data, ora)
        self.__tranzactie_repository.modifica(tranzactie)
        self.__undo_redo_service.add_undo_redo_operation(
            ModifyOperation(self.__tranzactie_repository, tranzactie_veche,
                            tranzactie))

    def cautare(self, text):
        """
        Cautare full text dupa parametrul text
        :param text: parametrul dupa care se cauta
        :return:
        """
        result = []
        for masina in self.__masina_repository.read():
            if text in str(masina.id_entitate) or \
                    text in masina.model or \
                    text in masina.garantie or \
                    text in str(masina.an_achizitie) or \
                    text in str(masina.km):
                result.append(masina)

        for card_client in self.__card_repository.read():
            if text in card_client.id_entitate or \
                    text in card_client.nume or \
                    text in card_client.prenume or \
                    text in str(card_client.cnp) or \
                    text in str(card_client.data_nastere) or \
                    text in str(card_client.data_inregistrare):
                result.append(card_client)

        return result

    def sterge_masina_tranzactie(self, id_car):
        """
        Sterge masina cu id-ul dat
        Sterge toate tranzactiile care contin masina cu id-ul dat
        :param id_car: id masina
        :return: None
        """
        masina = self.__masina_repository.read(id_car)
        lista = []
        self.__masina_repository.sterge(id_car)
        for tranzactie in self.__tranzactie_repository.read():
            if tranzactie.id_masina == id_car:
                lista.append(tranzactie)
                self.__tranzactie_repository.sterge(tranzactie.id_entitate)
        self.__undo_redo_service.add_undo_redo_operation(
            WaterfallDeleteOperation(self.__tranzactie_repository,
                                     self.__masina_repository,
                                     lista,
                                     masina))

    def suma_tranzactii_interval(self, interval_jos, interval_sus):
        """
        Returneaza tranzactiile cu suma cuprinsa intr-un interval
        :param interval_jos: numarul minim din interval
        :param interval_sus: numarul maxim din interval
        :return:
        """
        '''
        result = []
        for tranzactie in self.__tranzactie_repository.read():
            if int(interval_jos) <= \
                    tranzactie.suma_manopera + tranzactie.suma_piese \
                    <= int(interval_sus):
                result.append(tranzactie)
        return result
        '''
        lista = []
        for tranzactie in self.__tranzactie_repository.read():
            lista.append(tranzactie)
        result = filter(lambda x: int(interval_jos) <= x.suma_manopera +
                        x.suma_piese <= int(interval_sus), lista)
        return list(result)

    def my_sort(self, lista, key=None, reverse=False):
        if reverse is False:
            for i in range(len(lista) - 1):
                for j in range(i + 1, len(lista)):
                    if key(lista[i]) > key(lista[j]):
                        lista[i], lista[j] = lista[j], lista[i]
        else:
            for i in range(len(lista) - 1):
                for j in range(i + 1, len(lista)):
                    if key(lista[i]) < key(lista[j]):
                        lista[i], lista[j] = lista[j], lista[i]
        return lista

    def ordoneaza_masini_sumamanopera(self):
        """
        Returneaza masinile in ordine descrescatoare dupa suma manoperei
        :return:
        """
        sume_manopere_masini = {}
        rezultat = []
        for tranzactie in self.__tranzactie_repository.read():
            sume_manopere_masini[tranzactie.id_masina] \
                = tranzactie.suma_manopera
        for id_masina in sume_manopere_masini:
            suma = sume_manopere_masini[id_masina]
            rezultat.append(MasinaSumaManoperaViewModel(
                self.__masina_repository.read(id_masina),
                suma
            ))
        '''
        DACA VREAU SA AFISEZ SI MASINI FARA TRANZACTII(PLUS MODIFICA VIEW MODEL 
        SUMA.MANOPERA=LIST)
        for masina in self.__masina_repository.read():
            sume_manopere_masini[masina.id_entitate] = []
        for tranzactie in self.__tranzactie_repository.read():
            sume_manopere_masini[tranzactie.id_masina] \
                .append(tranzactie.suma_manopera)
        lista = [0]
        for id_masina in sume_manopere_masini:
            suma = sume_manopere_masini[id_masina]
            rezultat.append(MasinaSumaManoperaViewModel(
                self.__masina_repository.read(id_masina),
                suma if suma else lista
            ))
        '''

        return self.my_sort(rezultat,
                            key=lambda suma_man: suma_man.suma_manopera,
                            reverse=True)

    def ordoneaza_carduri_reducere(self):
        """
        Returneaza cardurile in ordine descrecatoare dupa reducere aplicata la
        suma manoperei
        :return:
        """
        sume_manopere = {}
        rezultat = []
        for tranzactie in self.__tranzactie_repository.read():
            sume_manopere[tranzactie.id_card_client] = tranzactie.suma_manopera
        for id_card_client in sume_manopere:
            suma = sume_manopere[id_card_client]
            rezultat.append(CardSumaManoperaViewModel(
                self.__card_repository.read(id_card_client),
                suma/9
            ))
        '''
        DACA VREAU SA AFISEZ SI CARDURILE FARA TRANZACTII(PLUS MODIFICA 
        VIEW MODEL REDUCERE = LIST)
        for card in self.__card_repository.read():
            sume_manopere[card.id_entitate] = []
        for tranzactie in self.__tranzactie_repository.read():
            sume_manopere[tranzactie.id_card_client]\
                .append(int(tranzactie.suma_manopera))
        lista = [0]
        for id_card_client in sume_manopere:
            rezultat.append(CardSumaManoperaViewModel(
                self.__card_repository.read(id_card_client),
                sume_manopere[id_card_client]
            ))
        '''

        return sorted(rezultat,
                      key=lambda reducere: reducere.reducere,
                      reverse=True)

    def stergere_tranzactie_data_interval(self, interval_jos, interval_sus):
        """
        Sterge toate tranzactiile cu data in intervalul de date dat
        :param interval_jos: data de inceput a intervalului de timp
        :param interval_sus: data de final a intervalului de timp
        :return:
        """
        lista = []
        for tranzactie in self.__tranzactie_repository.read():
            if interval_jos <= tranzactie.data <= interval_sus:
                lista.append(tranzactie)
                self.__tranzactie_repository.sterge(tranzactie.id_entitate)
                self.__undo_redo_service.add_undo_redo_operation(
                    MultiDeleteOperation(self.__tranzactie_repository, lista))
