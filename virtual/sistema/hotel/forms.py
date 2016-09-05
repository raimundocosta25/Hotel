# -*- coding: utf-8 -*-
from django import forms
from hotel.models import *

class FormularioHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = []
