from django.shortcuts import render, redirect
from .forms import AlgoForm, AutoForm, NewRegister
from .models import Algo, Auto

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

def subiralgo(request):
    if request.method=="POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user.username
            instance.save()
            return redirect('dashboard')
    else:
        form=AutoForm()
    return render(request, 'subiralgo.html',{
        'form':form
    })

def ver(request):
    lista_autos= Auto.objects.all()
    return render(request, 'ver.html', {
        'lista_autos': lista_autos
    })

def revisaralgo(request, pk):
    auto = Auto.objects.get(pk=pk)
    return render(request, 'revisaralgo.html', {
        'auto':auto
    })

def borraralgo(request, pk):
    if request.method == "POST":
        auto = Auto.objects.get(pk=pk)
        auto.delete()
    return redirect('ver')