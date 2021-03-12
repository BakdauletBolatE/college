from django.shortcuts import render
from .models import Specialization
# Create your views here.


def index(request):

    specializations = Specialization.objects.all()
    data = {
        'specializations':specializations
    }

    return render(request, 'specialization/index.html',data)

def detail(request,pk):

    specialization = Specialization.objects.get(id=pk)

    data = {
        'specialization':specialization
    }

    return render(request, 'specialization/single-page.html',data)