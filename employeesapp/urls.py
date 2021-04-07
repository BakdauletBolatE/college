from django.urls import path
from .views import indexG,indexT,tDetailView,gDetailView
urlpatterns = [
    path('govs/',indexG,name='indexG'),
    path('teachers/',indexT,name='indexT'),
    path('t/<int:pk>/',tDetailView,name="tDetailView"),
    path('g/<int:pk>/',gDetailView,name="gDetailView")
]