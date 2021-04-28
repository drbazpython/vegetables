from django.shortcuts import render, redirect, get_object_or_404
from vegetablesApp.forms import VegetablesAddForm
from vegetablesApp.models import Vegetables

# Create your views here.
def vegetables_home_view(request):
    vegetables = Vegetables.objects.all()
    context = {'vegetables': vegetables}
    return render(request,'vegetablesApp/home.html', context)

def vegetables_add_view(request):
    form = VegetablesAddForm()
    if request.method == 'POST':
        form = VegetablesAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')
    context={'form':form}
    return render(request,'vegetablesApp/add_veg.html', context)

def vegetables_list_view(request, id):
    vegetable = get_object_or_404(Vegetables, id=id)
    #vegetables = Vegetables.objects.all()
    context={'vegetable':vegetable}
    return render(request,'vegetablesApp/list_veg.html', context)