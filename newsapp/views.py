from django.shortcuts import render,redirect
from .models import NewsCategory, NewsPost
from django.urls import reverse
from .forms import NewsCommentForm
from django.contrib import messages
from page.models import PageCategory
# Create your views here.

def list_view(request):

    news = NewsPost.objects.all().order_by('-created_at')
    categories = NewsCategory.objects.order_by('-created_at')

    data = {
        'news':news,
        'categories':categories,
    }
    return render(request,'news/new-list.html',data)

def list_by_category(request, pk):

    news = NewsPost.objects.filter(category_id=pk).order_by('-created_at')
    categories = NewsCategory.objects.all().order_by('-created_at')
    active_category = NewsCategory.objects.get(id=pk)

    data = {
        'news':news,
        'categories':categories,
        'active_category':active_category
    }

    return render(request,'news/new-list.html',data)

def old_listView(request):

    news = NewsPost.objects.all()
    
    categories = NewsCategory.objects.all().order_by('-created_at')

    data = {
        'news':news,
        'categories':categories,
    }
    return render(request,'news/list.html',data)

def detailView(request,pk):

    new = NewsPost.objects.get(id=pk)
    comments = new.comments.filter(visible=True)
    form = NewsCommentForm()
    if request.method == "POST":
        form = NewsCommentForm(request.POST or None)

        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.author = request.user
            update_form.specialization = new
            update_form.save()
            messages.warning(request, 'Ваш коментарий успешно добавлен') # ignored

            return redirect(str(reverse('newsapp:detailView',args=[pk]))+"#review")

    data = {
        'form':form,
        'comments':comments,
        'new':new,
    }
   
    return render(request,'news/single-page.html',data)
