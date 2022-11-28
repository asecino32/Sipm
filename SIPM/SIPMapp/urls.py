from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.indexView,name="index"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('preguntas/',views.preguntasView,name="preguntas"),
    path('cuestionario_mat021_mv1/',views.cuestionario_mat021_mv1, name="cuestionario_mat021_mv1"),
    path("retroalimentación_mat021_mv1/", views.retroalimentación_mato21_mv1, name = "retro_mat021_mv1"),
    path("retroalimentación_mat021_iv1/", views.retroalimentación_mato21_iv1, name = "retro_mat021_iv1"),
    path('jugar/', views.jugar, name = "jugar" ),
    path('resultado/<int:pregunta_respondida_pk>/',views.resultado_pregunta, name='resultados'),
    path('tablero/',views.tablero, name = 'tablero'),
    path('jugar1/', views.jugar21i1, name = "jugar1" ),
    path('resultado1/<int:pregunta1_respondida1_pk>/',views.resultadopregunta21i1, name='resultados1'),
    path('cuestionario_mat022_mv2/',views.cuestionario_mat022_mv2, name="cuestionario_mat022_mv2"),
    path("retroalimentación_mat022_mv1/", views.retroalimentación_mato22_mv1, name = "retroalimentación_mato22_mv1"),
    ]