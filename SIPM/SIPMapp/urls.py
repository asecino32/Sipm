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
    path('cuestionario_mat021_iv1/',views.cuestionario_mat021_iv1, name="cuestionario"),
]