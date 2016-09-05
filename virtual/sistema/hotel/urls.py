from django.conf.urls import url
from hotel import views

urlpatterns = [
    url(r'^novo/$', views.HotelNew.as_view(), name='novo-hotel'),
]
