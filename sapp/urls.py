from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about-us/', about_us_view, name="about_url"),
    path('admission-rules/', admission_rules, name="admission_rules"),
    path('code-of-honor/', code_of_honor, name="code_of_honor_url"),
    path('login/', CollegeLoginView.as_view(), name="login"),
    path('register/', CollegeRegisterView.as_view(), name="register"),
    path('logout/', CollegeLogoutView.as_view(), name="logout"),
    path('appeal-send/', appealView, name='appealRoute')
]
