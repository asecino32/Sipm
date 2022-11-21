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
# model 2.
class ElegirRespuestaInline_MAT021_iv1(admin.TabularInline):

    can_delete = False
    model = ElegirRespuesta_MAT021_iv1
    max_num = ElegirRespuesta_MAT021_iv1.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta_MAT021_iv1.MAXIMO_RESPUESTA
    formset = ElegirInlineformset

class PreguntasAdmin_MAT021_iv1(admin.ModelAdmin):
    model = Pregunta_MAT021_iv1
    inlines = (ElegirRespuestaInline_MAT021_iv1,)
    list_display= ['texto',]
    search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin_MAT021_iv1(admin.ModelAdmin):
    list_display = ['pregunta','respuesta', 'correcta','puntaje_obtenido']
    
    class Meta:
        model = PreguntasRespondidas_MAT021_iv1

admin.site.register(PreguntasRespondidas_MAT021_iv1)
admin.site.register(Pregunta_MAT021_iv1,PreguntasAdmin_MAT021_iv1)
admin.site.register(ElegirRespuesta_MAT021_iv1)
admin.site.register(QuizUsuario_MAT021_iv1)
# Register your models here.