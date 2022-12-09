from django.urls import path

from .views import news_list_view, news_detail_view, list_by_category, list_gallery_view

urlpatterns = [
    path('', news_list_view, name="list_view"),
    path('news/<int:pk>/', news_detail_view, name="detail_view"),
    path('gallery/', list_gallery_view, name='list_gallery_view'),
    path('news-by-category/<int:pk>/', list_by_category, name="list_by_cat"),
]
