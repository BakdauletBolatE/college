from django.shortcuts import render
from django.urls import reverse_lazy
from specializationapp.models import Specialization
from employeesapp.models import Government
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from .forms import AuthUserForm,RegisterUserForm
from django.contrib.auth import authenticate, login
from newsapp.models import NewsPost
from django.utils.translation import activate, get_language_info
# Create your views here.

def index(request):

    specializations = Specialization.objects.all()[:3]
    imps = Government.objects.filter(isimp=1)[:3]
    news = NewsPost.objects.all()[:3]

    
    activate('ru')
    li = get_language_info('ru')
    print(li['name'], li['name_local'], li['name_translated'], li['bidi'])

    data = {
        'specializations':specializations,
        'imps':imps,
        'news':news
    }
    return render(request,'sapp/home.html',data)

def code_of_honor(request):
    return render(request,'pages/code_of_honor.html')

def admission_rules(request):
    return render(request,'pages/admission_rules.html')

def newEFormat(request):
    return render(request,'pages/newEFormat.html')
    
def ab2020(request):
    return render(request,'pages/2020ab.html')

def contact(request):
    return render(request,'sapp/contact.html')

def aboutUrl(request):
    return render(request,'sapp/about.html')

def internationalUrl(request):
    return render(request,'sapp/international.html')

class CollegeLoginView(LoginView):

    template_name = 'profile/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('sapp:index')

    def get_success_url(self):

        return self.success_url

class CollegeRegisterView(CreateView):

    template_name = 'profile/register.html'
    form_class = RegisterUserForm
    success_msg = "Вы успешно прошли регистрацию"
    success_url = reverse_lazy('sapp:index')

    def form_valid(self, form):
        form_valid = super().form_valid(form)        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return form_valid

    def get_success_url(self):

        return self.success_url
    

class CollegeLogoutView(LogoutView):

    next_page = '/'


    