from django.urls import path

from .views import list_view,old_listView,detailView,list_by_category

urlpatterns = [
    path('',list_view,name="listView"),
    path('old/',old_listView,name="listView"),
    path('news/<int:pk>/',detailView, name="detailView"),
    path('news-by-category/<int:pk>/',list_by_category, name="list_by_cat"),
    
]