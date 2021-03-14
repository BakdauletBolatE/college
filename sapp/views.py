from django.shortcuts import render
from django.urls import reverse_lazy
from specializationapp.models import Specialization
from employeesapp.models import Government
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import AuthUserForm,RegisterUserForm
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


class CollegeLoginView(LoginView):

    template_name = 'profile/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('sapp:index')

class CollegeRegisterView(CreateView):

    template_name = 'profile/register.html'
    form_class = RegisterUserForm
    success_msg = "Вы успешно прошли регистрацию"
    success_url = reverse_lazy('sapp:index')


    