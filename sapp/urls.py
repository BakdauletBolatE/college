from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('gallery/',galletyView,name="galleryView"),
    path('structure',structure,name="structure"),
    path('about-us/',aboutUrl,name="aboutUrl"),
    path('international/',internationalUrl,name="internationalUrl"),
    path('contacts/',contact,name="contact"),
    path('admission-rules/',admission_rules,name="admission_rules"),
    path('new-ent-format/',newEFormat,name="newEFormat"),
    path('2020ab/',ab2020,name="ab2020"),
    path('code_of_honor/',code_of_honor,name="code_of_honor"),
    path('login/',CollegeLoginView.as_view(),name="login"),
    path('register/',CollegeRegisterView.as_view(),name="register"),
    path('logout/',CollegeLogoutView.as_view(),name="logout")
]
