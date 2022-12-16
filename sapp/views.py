from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from specializationapp.models import Section, Specialization, Qualification, SubSection
from employeesapp.models import Government
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import AuthUserForm, RegisterUserForm, AppealForm
from django.contrib.auth import authenticate, login
from newsapp.models import NewsPost, GalleryPost
from .models import Abiturent
from django.contrib import messages


# Create your views here.


def index(request):
    specializations = Specialization.objects.all()
    news = NewsPost.objects.all().exclude(category_id=3).order_by('-created_at')[:3]

    data = {
        'specializations': specializations,
        'news': news
    }
    return render(request, 'home/index.html', data)

def code_of_honor(request):
    return render(request, 'sapp/code-of-honor.html')


def admission_rules(request):
    return render(request, 'pages/admission_rules.html')


def about_us_view(request):
    return render(request, 'sapp/about-us.html')


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


def appealView(request):

    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлено')
        else:
            messages.success(request, 'Что то пошло не так')

        return redirect('sapp:index')

