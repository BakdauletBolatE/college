from django.urls import path
from .views import list_government_view, list_employees_view, employees_detail_view

urlpatterns = [
    path('', list_employees_view, name='list_employees_view'),
    path('government/', list_government_view, name='list_government_view'),
    path('detail-employee/<int:pk>/<int:type>/', employees_detail_view, name="employees_detail_view"),
]
