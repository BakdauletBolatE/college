from page.models import PageCategory


def page_category(request):
    pageCats = PageCategory.objects.all().order_by('order')
    return {
        'pageCats':pageCats
    }