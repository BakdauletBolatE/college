from django.urls import path,include
from .views import index,detail,SubSectionView,SubSectionDetailView,SpecializationDetailView,QualificationDetailView
urlpatterns = [
    path('',index,name="index"),
    path('<int:pk>/',detail,name="detail"),
    path('subsection/',SubSectionView.as_view(),name="subectionview"),
    path('subsection/<int:id>',SubSectionDetailView.as_view(),name="subectiondview"),
    path('specialization/<int:id>',SpecializationDetailView.as_view(),name="SpecializationDetailView"),
    path('qualification/<int:id>',QualificationDetailView.as_view(),name="qualification")
]