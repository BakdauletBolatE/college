from django.urls import path
from .views import indexG,indexT,detailView
urlpatterns = [
    path('govs/',indexG,name='indexG'),
    path('teachers/',indexT,name='indexT'),
    path('d/<int:pk>/',detailView,name="detailView")
]