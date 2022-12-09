from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsCategory, NewsPost, GalleryPost
from django.urls import reverse
from .forms import NewsCommentForm
from django.contrib import messages


def list_by_category(request, pk):
    news = NewsPost.objects.filter(category_id=pk).order_by('-created_at')
    paginator = Paginator(news, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = NewsCategory.objects.all().order_by('-created_at')
    active_category = NewsCategory.objects.get(id=pk)
    data = {
        'page_obj': page_obj,
        'categories': categories,
        'active_category': active_category
    }

    return render(request, 'news/list.html', data)


def list_gallery_view(request):
    posts = GalleryPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }

    return render(request, 'news/gallery_list.html', data)


def news_list_view(request):
    news = NewsPost.objects.all()
    paginator = Paginator(news, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = NewsCategory.objects.all().order_by('-created_at')

    data = {
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'news/list.html', data)


def news_detail_view(request, pk):
    new = get_object_or_404(NewsPost, id=pk)
    comments = new.comments.filter(visible=True)
    categories = NewsCategory.objects.all().order_by('-created_at')
    form = NewsCommentForm()
    if request.method == "POST":
        form = NewsCommentForm(request.POST or None)

        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.author = request.user
            update_form.specialization = new
            update_form.save()
            messages.warning(request, 'Ваш коментарий успешно добавлен')  # ignored

            return redirect(str(reverse('newsapp:detailView', args=[pk])) + "#review")

    data = {
        'form': form,
        'comments': comments,
        'categories': categories,
        'object': new,
    }

    return render(request, 'news/detail.html', data)
