from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from .forms import AddRateForm,AddTaskForm,AddAnswerForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .decarators import role_reqiured,addTaskDecarator
from django.views import View
# Create your views here.


@role_reqiured()
def teacherprofile(request):

    teacher = request.user.teacher
    cemesters = Cemester.objects.all()
    weeks = Weekend.objects.all()

    if request.POST.get('cemester'):
        c_id  = request.POST.get('cemester')
    else:
        c_id = 1

    if request.POST.get('group'):
        g_id = request.POST.get('group')
    else:
        g_id = teacher.groups.first().id

    if request.POST.get('week'):
        w_id = request.POST.get('week')
    else:
        w_id = 1

    qs = Tasks.objects.filter(group_id=g_id,cemester_id=c_id,week_id=w_id)
    data = {
        'teacher':teacher,
        'cemesters':cemesters,
        'weeks':weeks,
        'c_id':c_id,
        'g_id':g_id,
        'w_id':w_id,
        'qs':qs,
    }
    return render(request,'examapp/hometeacher.html',data)

def teacherstat(request):

    teacher = request.user.teacher
    cemesters = Cemester.objects.all()

    if request.POST.get('cemester'):
        c_id  = request.POST.get('cemester')
    else:
        c_id = 1

    if request.POST.get('group'):
        g_id = request.POST.get('group')
    else:
        g_id = teacher.groups.first().id

    if request.POST.get('subject'):
        s_id = request.POST.get('subject')
    else:
        s_id = teacher.subject.first().id

    

    qs = Tasks.objects.filter(group_id=g_id,cemester_id=c_id,subject_id=s_id).order_by('week')
    qs2 = Answer.objects.filter(task_id=1)
    data = {
        'teacher':teacher,
        'cemesters':cemesters,
        'c_id':c_id,
        'g_id':g_id,
        's_id':s_id,
        'qs':qs,
        'qs2':qs2
    }
    return render(request,'examapp/teacherstat.html',data)


def studentprofile(request):

    student = request.user.student
    

    data = {
        'student':student,        
    }
    return render(request,'examapp/homestudent.html',data)

def studentrate(request):

    student = request.user.student
    cemesters = Cemester.objects.all()
    weeks = Weekend.objects.all()
    subjects = student.subject.all()

    if request.POST.get('cemester'):
        c_id  = request.POST.get('cemester')
    else:
        c_id = 1

   
    g_id = student.group.id

    if request.POST.get('subject'):
        s_id = request.POST.get('subject')
    else:
        s_id = student.subject.first().id

   
    
    
    cemester = Cemester.objects.get(id=c_id)
    subject = Subject.objects.get(id=s_id)


    qs = Tasks.objects.filter(group_id=g_id,cemester_id=c_id,subject=s_id)


    data = {
        'student':student,
        'cemesters':cemesters,
        'cemester':cemester,
        'weeks':weeks,
        'subjects':subjects,
        'subject':subject,
        'qs':qs,
        'c_id':c_id,
        's_id':s_id
        
    }
    return render(request,'examapp/studentrate.html',data)

def addRate(request):
   
    if request.method == 'POST':
        form = AddRateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(str(reverse('examapp:teacher')))



def addAnswer(request):

    if request.method == 'POST':
        form = AddAnswerForm(request.POST or None,request.FILES or None)
        print(form)
        if form.is_valid():
            form.save()
            return redirect(str(reverse('examapp:student')))



@addTaskDecarator()
def addTask(request):


    teacher = request.user.teacher
    cemesters = Cemester.objects.all()
    weeks = Weekend.objects.all()

    if request.method == 'POST':
        form = AddTaskForm(request.POST or None,request.FILES or None)

        if form.is_valid():
            group = form.cleaned_data['group']
            subject = form.cleaned_data['subject']
            cemester = form.cleaned_data['cemester']
            week = form.cleaned_data['week']
            user = form.cleaned_data['user']

            try:
                task = Tasks.objects.get(group_id=group,subject_id=subject,cemester_id=cemester,week_id=week,user_id=user)
                messages.warning(request, 'Такая задания уже существует')
                print('oo')
                return redirect(reverse('examapp:addTask'))
                

            except ObjectDoesNotExist:
                messages.success(request, 'Ваше задания успешно загружено')
                form.save()
                print('bb')
                return redirect(reverse('examapp:addTask'))
        

    data = {
        'teacher':teacher,
        'cemesters':cemesters,
        'weeks':weeks,
    }

    return render(request,'examapp/addTask.html',data)