from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from service_auto.models import Masina, Card, Tranzactie
from service_auto.serializers import MasinaSerializer, CardSerializer, TranzactieSerializer
from rest_framework.decorators import api_view

# CRUD MASINA


@api_view(['GET', 'POST', 'DELETE'])
def masina_list(request):
    if request.method == 'GET':
        masini = Masina.objects.all()

        id_masina = request.query_params.get('id', None)
        if id is not None:
            masini = masini.filter(id__icontains=id_masina)

        masini_serializer = MasinaSerializer(masini, many=True)
        return JsonResponse(masini_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        masini_data = JSONParser().parse(request)
        masini_serializer = MasinaSerializer(data=masini_data)
        if masini_serializer.is_valid():
            masini_serializer.save()
            return JsonResponse(masini_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(masini_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Masina.objects.all().delete()
        return JsonResponse({'message': '{} Masina was deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def masina_detail(request, pk):
    try:
        masini = Masina.objects.get(pk=pk)
    except Masina.objects.DoesNotExist:
        return JsonResponse({'message': 'The Masina does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        masini_serializer = MasinaSerializer(masini)
        return JsonResponse(masini_serializer.data)

    elif request.method == 'PUT':
        masini_data = JSONParser().parse(request)
        masini_serializer = MasinaSerializer(masini, data=masini_data)
        if masini_serializer.is_valid():
            masini_serializer.save()
            return JsonResponse(masini_serializer.data)
        return JsonResponse(masini_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        masini.delete()
        return JsonResponse({'message': 'Masina was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def masina_list_published(request):
    masini = Masina.objects.filter(published=True)

    if request.method == 'GET':
        masini_serializer = MasinaSerializer(masini, many=True)
        return JsonResponse(masini_serializer.data, safe=False)

# CRUD CARD


@api_view(['GET', 'POST', 'DELETE'])
def card_list(request):
    if request.method == 'GET':
        cards = Card.objects.all()

        id_card = request.query_params.get('id', None)
        if id is not None:
            cards = cards.filter(id__icontains=id_card)

        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        cards_data = JSONParser().parse(request)
        cards_serializer = CardSerializer(data=cards_data)
        if cards_serializer.is_valid():
            cards_serializer.save()
            return JsonResponse(cards_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cards_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} Card was deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk):
    try:
        cards = Card.objects.get(pk=pk)
    except Card.objects.DoesNotExist:
        return JsonResponse({'message': 'The Card does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        cards_serializer = CardSerializer(cards)
        return JsonResponse(cards_serializer.data)

    elif request.method == 'PUT':
        cards_data = JSONParser().parse(request)
        cards_serializer = CardSerializer(cards, data=cards_data)
        if cards_serializer.is_valid():
            cards_serializer.save()
            return JsonResponse(cards_serializer.data)
        return JsonResponse(cards_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cards.delete()
        return JsonResponse({'message': 'Card was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def card_list_published(request):
    cards = Card.objects.filter(published=True)

    if request.method == 'GET':
        cards_serializer = CardSerializer(cards, many=True)
        return JsonResponse(cards_serializer.data, safe=False)

# CRUD TRANZACTIE


@api_view(['GET', 'POST', 'DELETE'])
def tranzactie_list(request):
    if request.method == 'GET':
        tranzactii = Tranzactie.objects.all()

        id_tranzactie = request.query_params.get('id', None)
        if id is not None:
            tranzactii = tranzactii.filter(id__icontains=id_tranzactie)

        tranzactii_serializer = TranzactieSerializer(tranzactii, many=True)
        return JsonResponse(tranzactii_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        tranzactii_data = JSONParser().parse(request)
        tranzactii_serializer = TranzactieSerializer(data=tranzactii_data)
        if tranzactii_serializer.is_valid():
            tranzactii_serializer.save()
            return JsonResponse(tranzactii_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tranzactii_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tranzactie.objects.all().delete()
        return JsonResponse({'message': '{} Tranzactie was deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tranzactie_detail(request, pk):
    try:
        tranzactii = Tranzactie.objects.get(pk=pk)
    except Tranzactie.objects.DoesNotExist:
        return JsonResponse({'message': 'The Tranzactie does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tranzactii_serializer = TranzactieSerializer(tranzactii)
        return JsonResponse(tranzactii_serializer.data)

    elif request.method == 'PUT':
        tranzactii_data = JSONParser().parse(request)
        tranzactii_serializer = TranzactieSerializer(tranzactii, data=tranzactii_data)
        if tranzactii_serializer.is_valid():
            tranzactii_serializer.save()
            return JsonResponse(tranzactii_serializer.data)
        return JsonResponse(tranzactii_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tranzactii.delete()
        return JsonResponse({'message': 'Tranzactie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def tranzactie_list_published(request):
    tranzactii = Tranzactie.objects.filter(published=True)

    if request.method == 'GET':
        tranzactii_serializer = TranzactieSerializer(tranzactii, many=True)
        return JsonResponse(tranzactii_serializer.data, safe=False)
