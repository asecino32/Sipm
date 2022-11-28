from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class Pregunta(models.Model):

	NUMER_DE_RESPUESTAS_PERMITIDAS = 1

	texto = models.TextField(verbose_name='Texto de la pregunta')
	max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=3, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.texto 


class ElegirRespuesta(models.Model):

	MAXIMO_RESPUESTA = 4

	pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')


	def __str__(self):
		return self.texto

class QuizUsuario(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
		intento.save()

	def obtener_nuevas_preguntas(self):
		respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
		preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
		if not preguntas_restantes.exists():
			return None
		return random.choice(preguntas_restantes)


	def validar_intento(self, pregunta_respondida, respuesta_selecionada):
		if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
			return

		pregunta_respondida.respuesta_selecionada = respuesta_selecionada
		if respuesta_selecionada.correcta is True:
			pregunta_respondida.correcta = True
			pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
			pregunta_respondida.respuesta = respuesta_selecionada

		else:
			pregunta_respondida.respuesta = respuesta_selecionada

		pregunta_respondida.save()

		self.actualizar_puntaje()

	def actualizar_puntaje(self):
		puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
			models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

		self.puntaje_total = puntaje_actualizado
		self.save()

class PreguntasRespondidas(models.Model):
	quizUser = models.ForeignKey(QuizUsuario, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
	correcta  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)

class Pregunta21i1(models.Model):

	NUMER_DE_RESPUESTAS_PERMITIDAS = 1

	texto = models.TextField(verbose_name='Texto de la pregunta')
	max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=3, decimal_places=2, max_digits=6)

	def __str__(self):
		return self.texto


class ElegirRespuesta21i1(models.Model):

	MAXIMO_RESPUESTA = 4

	pregunta = models.ForeignKey(Pregunta21i1, related_name='opciones21iv1', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')

	def __str__(self):
		return self.texto

class QuizUsuario21i1(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas21i1(pregunta1=pregunta, quizUser1=self)
		intento.save()

	def obtener_nuevas_preguntas(self):
		respondidas = PreguntasRespondidas21i1.objects.filter(quizUser1=self).values_list('pregunta1__pk', flat=True)
		preguntas_restantes = Pregunta21i1.objects.exclude(pk__in=respondidas)
		if not preguntas_restantes.exists():
			return None
		return random.choice(preguntas_restantes)


	def validar_intento(self, pregunta_respondida1, respuesta_selecionada1):
		if pregunta_respondida1.pregunta_id != respuesta_selecionada1.pregunta_id:
			return

		pregunta_respondida1.respuesta_selecionada1 = respuesta_selecionada1
		if respuesta_selecionada1.correcta1 is True:
			pregunta_respondida1.correcta1 = True
			pregunta_respondida1.puntaje_obtenido1 = respuesta_selecionada1.pregunta21i1.max_puntaje
			pregunta_respondida1.respuesta1 = respuesta_selecionada1

		else:
			pregunta_respondida1.respuesta1 = respuesta_selecionada1

		pregunta_respondida1.save()

		self.actualizar_puntaje1()

	def actualizar_puntaje1(self):
		puntaje_actualizado1 = self.intentos21i1.filter(correcta=True).aggregate(
			models.Sum('puntaje_obtenido1'))['puntaje_obtenido1__sum']

		self.puntaje_total1 = puntaje_actualizado1
		self.save()

class PreguntasRespondidas21i1(models.Model):
	quizUser1 = models.ForeignKey(QuizUsuario21i1, on_delete=models.CASCADE, related_name='intentos21i')
	pregunta1 = models.ForeignKey(Pregunta21i1, on_delete=models.CASCADE)
	respuesta1 = models.ForeignKey(ElegirRespuesta21i1, on_delete=models.CASCADE, null=True)
	correcta1  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido1 = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)

