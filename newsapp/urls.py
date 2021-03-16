from django.urls import path

from .views import listView,detailView

urlpatterns = [
    path('',listView,name="listView"),
    path('news/<int:pk>/',detailView, name="detailView"),
]