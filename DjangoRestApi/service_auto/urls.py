from django.conf.urls import url

import service_auto.views as views

urlpatterns = [
    url(r'^api/service_auto/masina_list.$', views.masina_list),
    url(r'^api/service_auto/masina_detail/(?P<pk>[0-9]+)$', views.masina_detail),
    url(r'^api/service_auto/masina_list_published$', views.masina_list_published),
    url(r'^api/service_auto/card_list.$', views.card_list),
    url(r'^api/service_auto/card_detail/(?P<pk>[0-9]+)$', views.card_detail),
    url(r'^api/service_auto/card_list_published$', views.card_list_published),
    url(r'^api/service_auto/tranzactie_list.$', views.tranzactie_list),
    url(r'^api/service_auto/tranzactie_detail/(?P<pk>[0-9]+)$', views.tranzactie_detail),
    url(r'^api/service_auto/tranzactie_list_published$', views.tranzactie_list_published)

]
