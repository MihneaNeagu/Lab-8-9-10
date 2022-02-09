from django.db import models


class Masina(models.Model):
    objects = models.Manager()
    model = models.CharField(max_length=70, blank=False, default='')
    an = models.IntegerField(blank=False, default='0')
    km = models.IntegerField(blank=False, default='0')
    garantie = models. BooleanField(default='False')


class Card(models.Model):
    objects = models.Manager()
    nume = models.CharField(max_length=70, blank=False, default='')
    prenume = models.CharField(max_length=70, blank=False, default='')
    cnp = models.PositiveBigIntegerField(blank=False, default='')
    data_nastere = models.CharField(max_length=40, blank=False, default='')
    data_inregistrare = models.CharField(max_length=40, blank=False, default='')


class Tranzactie(models.Model):
    objects = models.Manager()
    id_masina = models.CharField(max_length=70, blank=False, default='')
    id_card_client = models.CharField(max_length=70, blank=False, default='')
    suma_piese = models.IntegerField(blank=False, default='0')
    suma_manopera = models.IntegerField(blank=False, default='0')
    data_tranzactie = models.CharField(max_length=40, blank=False, default='')
    ora = models.CharField(max_length=70, blank=False, default='00:00')
