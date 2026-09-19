from django.http import HttpResponse
from django.shortcuts import render, redirect

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

def menu_delete(request,id):
    data = Menu.objects.get(id=id)
    print(data)
    data.delete()
    return redirect('menu_view')

def menu_update(request,id):
    data = Menu.objects.get(id = id)
    print(data)
    form = menuForm(instance=data)

    if request.method == 'POST':
        form = menuForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('menu_view')

    return render(request,'menu_update.html',{'data':form})