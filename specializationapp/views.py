from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Specialization
from .forms import SpecializationCommentForm
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def index(request):

    specializations = Specialization.objects.all()
    data = {
        'specializations':specializations
    }

    return render(request, 'specialization/index.html',data)

def detail(request,pk):

    specialization = Specialization.objects.get(id=pk)
    comments = specialization.comments.filter(visible=True)
    form = SpecializationCommentForm()
    if request.method == "POST":
        form = SpecializationCommentForm(request.POST or None)

        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.author = request.user
            update_form.specialization = specialization
            update_form.save()
            messages.warning(request, 'Ваш отзыв ожидает модераций: Спасибо за отклик') # ignored

            return redirect(str(reverse('specapp:detail',args=[pk]))+"#review")

    data = {
        'form':form,
        'comments':comments,
        'specialization':specialization
    }

    return render(request, 'specialization/single-page.html',data)

