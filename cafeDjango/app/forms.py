from django import forms 
from .models import Fazenda, AreaPlantio, Talhoes, Usuario

class FazendaFormulario(forms.ModelForm):
    class Meta:
        model = Fazenda
        fields = '__all__'

class AreaPlantioFormulario(forms.ModelForm):
    class Meta:
        model = AreaPlantio
        fields = '__all__'

class TalhoesFormulario(forms.ModelForm):
    class Meta:
        model = Talhoes
        fields = '__all__'