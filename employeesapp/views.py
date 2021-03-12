from django.shortcuts import render
from .models import Government
# Create your views here.


def indexG(request):

    imps = Government.objects.all()

    data = {
        'imps':imps
    }
    return render(request,'government/index.html',data)