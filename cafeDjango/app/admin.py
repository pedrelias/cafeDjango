from django.contrib import admin
from app.models import *
from .forms import FazendaFormulario, AreaPlantioFormulario, TalhoesFormulario

class AreaInline(admin.TabularInline):
    model = AreaPlantio
    form = AreaPlantioFormulario
    extra = 1

class TalhoesInline(admin.TabularInline):
    model = Talhoes
    form = TalhoesFormulario
    extra = 1

class FazendasAdmin(admin.ModelAdmin):
    inlines = [AreaInline, TalhoesInline]

admin.site.register(Cidade)
admin.site.register(Cargo)
admin.site.register(Usuario)
admin.site.register(Fazenda, FazendasAdmin)
admin.site.register(Talhoes)
admin.site.register(TexturaSolo)
admin.site.register(AnaliseSolo)
admin.site.register(Exportadora)

