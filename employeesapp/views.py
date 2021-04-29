from page.models import PageCategory
from django.shortcuts import render
from .models import Government,Employees
# Create your views here.


def indexG(request):

    imps = Government.objects.order_by('id').all()
    pageCats = PageCategory.objects.all()
    data = {
        'imps':imps,
        'pageCats':pageCats
    }
    return render(request,'government/index.html',data)

def indexT(request):

    imps = Employees.objects.all()
    pageCats = PageCategory.objects.all()

    data = {
        'imps':imps,
        'pageCats':pageCats
    }
    return render(request,'government/tindex.html',data)

def tDetailView(request,pk):
    pageCats = PageCategory.objects.all()

    government = Employees.objects.get(id=pk)

    data = {
        'government':government,
        'pageCats':pageCats
    }
    return render(request,'government/tsingle-page.html',data)

def gDetailView(request,pk):
    pageCats = PageCategory.objects.all()
    government = Government.objects.get(id=pk)

    data = {
        'government':government,
        'pageCats':pageCats
    }
    return render(request,'government/single-page.html',data)