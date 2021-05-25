from page.models import PageCategory, Page
from django.shortcuts import render
from django.urls import reverse_lazy
from specializationapp.models import Section, Specialization
from employeesapp.models import Government
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login
from newsapp.models import NewsPost, GalleryPost
from .models import Abiturent


# Create your views here.


def index(request):
    specializations = Specialization.objects.all()[:3]
    imps = Government.objects.filter(isimp=1).order_by('order')[:3]
    news = NewsPost.objects.all()[:3]

    data = {
        'specializations': specializations,
        'imps': imps,
        'news': news,
    }
    return render(request, 'sapp/home.html', data)


def structure(request):
    section = Section.objects.all()
    data = {
        'sections': section,
    }
    return render(request, 'sapp/strucrure.html', data)


def code_of_honor(request):
    return render(request, 'pages/code_of_honor.html')


def admission_rules(request):
    return render(request, 'pages/admission_rules.html')


def newEFormat(request):
    return render(request, 'pages/newEFormat.html')


def contact(request):
    return render(request, 'sapp/contact.html')


def aboutUrl(request):
    return render(request, 'sapp/about.html')


def galletyView(request):
    galleries = GalleryPost.objects.all().order_by('-created_at')
    data = {
        'galleries': galleries,
    }
    return render(request, 'pages/gallery.html', data)


def internationalUrl(request):
    return render(request, 'sapp/international.html')


def pageView(request, pk):
    page = Page.objects.get(id=pk)
    data = {
        'page': page,
    }
    return render(request, 'sapp/pageView.html', data)


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


def abiturent2021(request):
    abiturent = Abiturent.objects.first()
    data = {
        'abiturent': abiturent
    }
    return render(request, 'sapp/enroller.html', data)
