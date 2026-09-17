from django.http import HttpResponse
from django.shortcuts import render

from new_app.forms import menuForm
from new_app.models import Menu


# Create your views here.
def home(request):
    return render(request,'index.html')
# def dash(request):
#     return render(request,'dash.html')

def menu_data(request):
    form = menuForm()
    if request.method == 'POST':
        form = menuForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request,'menu_data.html',{'form':form})

def menu_view(request):
    data = Menu.objects.all()
    return render(request,'display.html',{'data':data})

def new(request):
    form = menuForm()
    if request.method == 'POST':
        form = menuForm(request.POST)
    if form.is_valid():
            form.save()

    return render(request, 'new.html', {'form': form})