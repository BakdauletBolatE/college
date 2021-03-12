from django.urls import path
from .views import indexG
urlpatterns = [
    path('gov/',indexG,name='indexG'),
]