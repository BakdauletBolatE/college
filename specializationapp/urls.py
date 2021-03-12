from django.urls import path,include
from .views import index,detail
urlpatterns = [
    path('',index,name="index"),
    path('<int:pk>/',detail,name="detail")
]