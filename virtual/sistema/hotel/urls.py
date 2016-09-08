from django.conf.urls import url
from hotel import views

urlpatterns = [
    url(r'^newHotel/$', views.HotelNew.as_view(), name='newHotel-hotel'),
    url(r'^newCheck/$', views.CheckNew.as_view(), name='newCheck-hotel'),
    url(r'^newItens/$', views.ItensNew.as_view(), name='newItens-hotel'),
]
