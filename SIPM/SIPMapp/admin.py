from django.contrib import admin
from .models import Pregunta,  ElegirRespuesta, PreguntasRespondidas, QuizUsuario
from .forms import ElegirInlineformset

class ElegirRespuestaInline(admin.TabularInline):

    can_delete = False
    model = ElegirRespuesta
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
    formset = ElegirInlineformset

class PreguntasAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInline,)
    list_display= ['texto',]
    search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta','respuesta', 'correcta','puntaje_obtenido']
    
    class Meta:
        model = PreguntasRespondidas

admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta,PreguntasAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(QuizUsuario)
# Register your models here.
