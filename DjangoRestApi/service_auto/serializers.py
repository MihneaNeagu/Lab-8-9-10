from rest_framework import serializers
from service_auto.models import Masina, Card, Tranzactie


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id',
                  'nume',
                  'prenume',
                  'cnp',
                  'data_nastere',
                  'data_inregistrare'
                  )


class MasinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masina
        fields = ('id',
                  'model',
                  'an',
                  'km',
                  'garantie'
                  )


class TranzactieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranzactie
        fields = ('id',
                  'id_masina',
                  'id_card_client',
                  'suma_piese',
                  'suma_manopera',
                  'data_tranzactie',
                  'ora'
                  )
