from django.shortcuts import render


# Create your views here.
def vegetables_home_view(request):
    context={}
    return render(request,'vegetablesApp/home.html', context)

def vegetables_add_view(request):
    context={}
    return render(request,'vegetablesApp/add_veg.html', context)

def vegetables_list_view(request):
    context={}
    return render(request,'vegetablesApp/list_veg.html', context)