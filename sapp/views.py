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
from django.utils.translation import gettext


# Create your views here.


def index(request):
    specializations = Specialization.objects.all()
    news = NewsPost.objects.all().exclude(category_id=3).order_by('-created_at')[:3]
    slides = [
        {
            'title': gettext('Добро пожаловать'),
            'pre_title': gettext('Высший педагогический колледж'),
            'description': gettext('Мир без горизонтов, мир новых идей и возможностей'),
            'image': gettext('images/slider-1920-1.png')
        },
        {
            'title': gettext('Каждый день'),
            'pre_title': gettext('Высший педагогический колледж'),
            'description': gettext('Новые воспоминаний'),
            'image': gettext('images/slider-1920-2.png')
        }
    ]

    about_contents = [
        {
            'id': 'about-edu',
            'text': gettext(
                "Высший педагогический колледж Shymkent – один из престижных учебных заведений Южного региона Республики Казахстан, готовящий педагогических специалистов среднего звена. Удовлетворяя потребности и спросы разных отраслей науки и рынка труда в квалифицированных специалистах, Высший педагогический колледж Shymkent доказал свой статус и конкурентоспособность на рынке труда современного мира.")
        },
        {
            'id': 'about-mission',
            'text': gettext(
                "Воспитание всесторонне гармонично развитой личности на основе общечеловеческих и национальных ценностей. Вносить свой вклад в модернизацию системы профессионального обучения на основе трехъязычной и модульной компетенции. Всестороннее использование инновационных технологий в учебном и воспитательном процессе колледжа.")
        },
        {
            'id': 'about-vision',
            'text': gettext(
                "Формирование научно-интеллектуальной и информационно-культурной среды конкурентоспособных специалистов с инновационными мировозрениями. Стратегический путь колледжа направлена на качественное и количественное усовершенствование показателей образовательной деятельности, ресурсное обеспечение потребностей обучающихся, создание благоприятной среды для работы персонала и для получения качественного образования студентов. Ссылаясь на актуальные направления осуществления государственной программы за 2011-2020 гг., были определены модернизованные направления развития нашего колледжа")
        }
    ]

    data = {
        'specializations': specializations,
        'news': news,
        'slides': slides,
        'mission_text': gettext(
            'Воспитание всесторонне гармонично развитой личности на основе общечеловеческих и национальных ценностей'),
        'pol_text': gettext(
            'формирование научно-интеллектуальной и информационно-культурной среды конкурентоспособных специалистов с инновационными мировозрениями.'),
        'history_text': gettext(
            'Основателем и первым президентом учреждения «Высший Педагогический колледж «Shynkent» является – Юнусов Бахтияр Саидович (1954-2010 г.г.) – профессор'),
        'about_contents': about_contents
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
