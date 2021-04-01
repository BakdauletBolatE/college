from django.shortcuts import render
from .models import Government,Employees
# Create your views here.


def indexG(request):

    imps = Government.objects.all()

    data = {
        'imps':imps
    }
    return render(request,'government/index.html',data)

def indexT(request):

    imps = Employees.objects.all()

    data = {
        'imps':imps
    }
    return render(request,'government/index.html',data)

def detailView(request,pk):

    government = Employees.objects.get(id=pk)

    data = {
        'government':government
    }
    return render(request,'government/single-page.html',data)