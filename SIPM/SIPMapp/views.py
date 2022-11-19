from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NewRegister
from .models import QuizUsuario, Pregunta, PreguntasRespondidas

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def registerView(request):
    if request.method == "POST":
        form = NewRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = NewRegister()
    
    return render(request,'registration/register.html',{'form':NewRegister})

def dashboardView(request):
    return render(request,'dashboard.html')

def preguntasView(request):
    return render(request,'preguntas.html')
def cuestionario_mat021_iv1(request):
    return render(request,'cuestionarios/cuestionario_mat021_iv1.html')
def retroalimentación_mato21_iv1(request):
    return render(request,'cuestionarios/retroalimentación_cuestionario_mat021_iv1.html')

def jugar(request):

    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user) 

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        repuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=repuesta_pk)
        
        except ObjectDoesNotExist:
            raise Http404
        
        QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)

        return redirect('resultado', pregunta_respondida.pk)
    
    else:
        pregunta = QuizUser.obtener_nuevas_preguntas()
        if pregunta is not None:
                QuizUser.crear_intentos(pregunta)

        context = {
            'pregunta': pregunta
        }
    return render(request, 'cuestionarios/jugar.html', context)

def resultado_preguntas(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk= pregunta_respondida_pk)

    context = {
        'respondida':respondida
    }
    return render(request, 'cuestionarios/jugar.html', context)