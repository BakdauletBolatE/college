from django.urls import path,include
from .views import index,aboutUrl,contact

urlpatterns = [
    path('',index,name="index"),
    path('about-us/',aboutUrl,name="aboutUrl"),
    path('contacts/',contact,name="contact")
]
