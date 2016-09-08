from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from hotel.models import *
from hotel.forms import *


# Create your views here.

class HotelNew(CreateView):
    model = Hotel
    form_class = FormularioHotel
    template_name = 'hotel/novoHotel.html'
    success_url = reverse_lazy('newHotel-hotel')

class CheckNew(CreateView):
    model = Check
    form_class = FormularioCheck
    template_name = 'hotel/novoCheck.html'
    success_url = reverse_lazy('newCheck-hotel')

class ItensNew(CreateView):
    model = Itens
    form_class = FormularioItens
    template_name = 'hotel/novoItens.html'
    success_url = reverse_lazy('newItens-hotel')
