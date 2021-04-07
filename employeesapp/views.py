from django.shortcuts import render
from .models import Government,Employees
# Create your views here.


def indexG(request):

    imps = Government.objects.order_by('id').all()

    data = {
        'imps':imps
    }
    return render(request,'government/index.html',data)

def indexT(request):

    imps = Employees.objects.all()

    data = {
        'imps':imps
    }
    return render(request,'government/tindex.html',data)

def tDetailView(request,pk):

    government = Employees.objects.get(id=pk)

    data = {
        'government':government
    }
    return render(request,'government/tsingle-page.html',data)

def gDetailView(request,pk):

    government = Government.objects.get(id=pk)

    data = {
        'government':government
    }
    return render(request,'government/single-page.html',data)