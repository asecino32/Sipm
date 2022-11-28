from django.contrib import admin
from .models import Pregunta,  ElegirRespuesta, PreguntasRespondidas, QuizUsuario, Pregunta21i1, ElegirRespuesta21i1, QuizUsuario21i1, PreguntasRespondidas21i1, QuizUsuario
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


class ElegirRespuestaInline21i1(admin.TabularInline):

    can_delete = False
    model = ElegirRespuesta21i1
    max_num = ElegirRespuesta21i1.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta21i1.MAXIMO_RESPUESTA
    formset = ElegirInlineformset

class PreguntasAdmin21i1(admin.ModelAdmin):
    model = Pregunta21i1
    inlines = (ElegirRespuestaInline21i1,)
    list_display= ['texto',]
    search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin_MAT021_iv1(admin.ModelAdmin):
    list_display = ['pregunta1','respuesta1', 'correcta1','puntaje_obtenido1']
    
    class Meta:
        model = PreguntasRespondidas21i1

admin.site.register(PreguntasRespondidas21i1)
admin.site.register(Pregunta21i1, PreguntasAdmin21i1)
admin.site.register(ElegirRespuesta21i1)
admin.site.register(QuizUsuario21i1)
# Register your models here.