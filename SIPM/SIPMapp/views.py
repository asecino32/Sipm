from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NewRegister
from .models import QuizUsuario, Pregunta, PreguntasRespondidas, QuizUsuario21i1, Pregunta21i1, PreguntasRespondidas21i1

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
def cuestionario_mat021_mv1(request):
    return render(request,'cuestionarios/cuestionario_mat021_mv1.html')
def cuestionario_mat022_mv2(request):
    return render(request,'cuestionarios/cuestionario_mat022_mv2.html')
def retroalimentación_mato21_mv1(request):
    return render(request,'cuestionarios/retroalimentación_cuestionario_mat021_mv1.html')
def retroalimentación_mato21_iv1(request):
    return render(request,'cuestionarios/retroalimentación_cuestionario_mat021_iv1.html')
def retroalimentación_mato22_mv1(request):
    return render(request,'cuestionarios/retroalimentación_cuestionario_mat022_mv1.html')


def tablero(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {

		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}

	return render(request, 'cuestionarios/tablero.html', context)

def jugar(request):

	QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('resultados', pregunta_respondida.pk)

	else:
		pregunta = QuizUser.obtener_nuevas_preguntas()
		if pregunta is not None:
			QuizUser.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, 'cuestionarios/jugar.html', context)



def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'cuestionarios/resultados.html', context)

def jugar21i1(request):

	QuizUser1, created = QuizUsuario21i1.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta21_pk = request.POST.get('pregunta21_pk')
		pregunta_respondida = QuizUser1.intentos21i.select_related('pregunta21').get(pregunta1__pk=pregunta21_pk)
		respuesta21_pk = request.POST.get('respuesta21_pk')

		try:
			opcion_selecionada = pregunta_respondida.Pregunta21i1.opciones21iv1.get(pk=respuesta21_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUser1.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('resultado1', pregunta_respondida.pk)

	else:
		pregunta21iv1= QuizUser1.obtener_nuevas_preguntas()
		if pregunta21iv1 is not None:
			QuizUser1.crear_intentos(pregunta21iv1)

		context = {
			'pregunta21iv1':pregunta21iv1
		}

	return render(request, 'cuestionarios/jugar1.html', context)



def resultadopregunta21i1(request, pregunta_respondida_pk):
	respondida1 = get_object_or_404(PreguntasRespondidas21i1, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida1
	}
	return render(request, 'cuestionarios/resultados1.html', context)

