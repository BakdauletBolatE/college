from django.urls import path,include
from .views import index,aboutUrl,contact,CollegeLoginView,CollegeRegisterView

urlpatterns = [
    path('',index,name="index"),
    path('about-us/',aboutUrl,name="aboutUrl"),
    path('contacts/',contact,name="contact"),
    path('login/',CollegeLoginView.as_view(),name="login"),
    path('register/',CollegeRegisterView.as_view(),name="register")
]
