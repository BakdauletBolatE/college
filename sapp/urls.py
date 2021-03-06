from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('old/',old_index),
    path('gallery/', galletyView, name="galleryView"),
    path('structure/', structure, name="structure"),
    path('about-us/', aboutUrl, name="aboutUrl"),
    path('international/', internationalUrl, name="internationalUrl"),
    path('contacts/', contact, name="contact"),
    path('admission-rules/', admission_rules, name="admission_rules"),
    path('new-ent-format/', newEFormat, name="newEFormat"),
    path('abiturent/', abiturent2021, name="abiturent"),
    path('code_of_honor/', code_of_honor, name="code_of_honor"),
    path('page/<int:pk>', pageView, name="pageView"),
    path('login/', CollegeLoginView.as_view(), name="login"),
    path('register/', CollegeRegisterView.as_view(), name="register"),
    path('logout/', CollegeLogoutView.as_view(), name="logout"),
    path('appeal-send/', appealView, name='appealRoute')
]
