from django.shortcuts import redirect, render

from .forms import NewRegister

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
