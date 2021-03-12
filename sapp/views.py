from django.shortcuts import render
from specializationapp.models import Specialization
from employeesapp.models import Government
# Create your views here.

def index(request):

    specializations = Specialization.objects.all()[:3]
    imps = Government.objects.filter(isimp=1)[:3]

    data = {
        'specializations':specializations,
        'imps':imps
    }
    return render(request,'sapp/home.html',data)

def contact(request):

    return render(request,'sapp/contact.html')

def aboutUrl(request):

    return render(request,'sapp/about.html')


    