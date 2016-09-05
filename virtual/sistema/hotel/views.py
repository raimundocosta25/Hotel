from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from hotel.models import *
from hotel.forms import *


# Create your views here.

class HotelNew(CreateView):
    model = Hotel
    form_class = FormularioHotel
    template_name = 'hotel/novoHotel.html'
    success_url = reverse_lazy('novo-hotel')
