
from django.urls import path,include
from .views import *


urlpatterns = [
    path('teacher/',teacherprofile,name="teacher"),
    path('student/',studentprofile,name="student"),
    path('srate/',studentrate,name="srate"),
    path('tstat/',teacherstat,name="tstat"),
    path('searhtasks/',tasksbyweek,name="stask"),
    path('addrate/',addRate,name="addRate"),
    path('task/add/',addTask,name="addTask"),
    path('answer/add/',addAnswer,name="addAnswer")
]