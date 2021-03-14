from django.shortcuts import render
from .models import NewsCategory, NewsPost

# Create your views here.

def listView(request):

    news = NewsPost.objects.all()
    categories = NewsCategory.objects.all()

    data = {
        'news':news,
        'categories':categories
    }
    return render(request,'news/list.html',data)