from django.views.generic.base import View
from django.views.generic.edit import DeleteView
from page.forms import PageCategoryForm, PageForm, WidgetPhotoForm, WidgetTextForm,WidgetOnlyTextForm
from page.models import Widget,WidgetGalery,WidgetGalleryPhotos, WidgetOnlyText, WidgetPhoto, WidgetText
from django.shortcuts import get_object_or_404, render,redirect
from .models import Page, PageCategory
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse,reverse_lazy
import json
from django.contrib.auth.mixins import PermissionRequiredMixin

import operator
from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(operator.attrgetter('is_staff'))

# Create your views here.

class WidgetTextUpdateView(PermissionRequiredMixin, View):

    def post(self,request,pk):

        widget = json.loads(request.body)
        type = widget['type']
 
        if type == "widgettext":
            widgetObject = get_object_or_404(WidgetText,id=pk)
            if widgetObject:
                widgetObject.title = widget['title']
                widgetObject.description = widget['description']
                widgetObject.save()
        
        if type == "widgetonlytext":
            widgetObject = get_object_or_404(WidgetOnlyText,id=pk)
            if widgetObject:
                widgetObject.description = widget['description']
                widgetObject.save()

        if type == "widgetphoto":
            widgetObject = get_object_or_404(WidgetPhoto,id=pk)
            if widgetObject:
                widgetObject.title = widget['title']
                widgetObject.description = widget['description']
                widgetObject.save()

        return HttpResponse("Hello")

class PageCategoryListView(PermissionRequiredMixin, ListView):
    redirect_field_name = '/'
    model = PageCategory
    template_name = 'page/category_page_list.html'
    permission_required = ('page.add_pagecategory')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PageCategory.objects.all().order_by('order')
        return context

class PageListView(PermissionRequiredMixin, ListView):
    redirect_field_name = '/'
    model = Page
    context_object_name = 'pages'
    template_name = 'page/page_list.html'
    permission_required = ('page.add_pagecategory')

    def get_queryset(self):
        return Page.objects.filter(category_id=self.kwargs['pk']).order_by('order')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['category'] = PageCategory.objects.get(id=id)
        context['categories'] = PageCategory.objects.all().order_by('order')
        return context

class PageDetailView(PermissionRequiredMixin, DetailView):
    model = Page
    context_object_name = 'page'
    template_name = 'page/pageDetail.html'
    permission_required = ('page.add_pagecategory')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pageWidgetsArray = []
        page = context['page']
        pageWidgets = Widget.objects.filter(page=page).order_by('order')
        context['pageWidgets'] = pageWidgets
        return context

class PageCreateView(PermissionRequiredMixin, CreateView):

    model = Page
    template_name = 'page/page_form.html'
    form_class = PageForm
    permission_required = ('page.add_pagecategory')

class PageUpdateView(UpdateView):
    permission_required = ('page.add_pagecategory')

    model = Page
    template_name = 'page/page_form.html'
    form_class = PageForm


class PageDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('page.add_pagecategory')

    model = Page
    template_name = "page/page_confirm_delete.html"

    def get_success_url(self):    
        return reverse_lazy('pageListView', kwargs = {'pk': self.kwargs['cat_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_id'] = self.kwargs['cat_id']
        return context
    

class PageCategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('page.add_pagecategory')

    model = PageCategory
    form_class = PageCategoryForm
    template_name = 'page/pageCategory_form.html'

class PageCategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('page.add_pagecategory')

    model = PageCategory
    template_name = 'page/pageCategory_form.html'
    form_class = PageCategoryForm

def orderedPages(request):

    if request.method == "POST":
        pages = json.loads(request.body)
    
        for b in pages:
            page = get_object_or_404(Page, id=int(b['pk']))
            page.order = b['order']
            page.save()
        return HttpResponse('saved')


def orderedCatPages(request):
    if request.method == "POST":
        pages = json.loads(request.body)

        for b in pages:
            page = get_object_or_404(PageCategory, id=int(b['pk']))
            page.order = b['order']
            page.save()
        return HttpResponse('saved')


def orderedWidgets(request):

    if request.method == "POST":
        widgets = json.loads(request.body)
    
        for b in widgets:
            page = get_object_or_404(Widget, id=int(b['pk']))
            page.order = b['order']
            page.save()
        return HttpResponse('saved')


def addWidget(request,*args,**kwargs):

    page = kwargs['pk']
    typeWidget = request.POST.get('type')

    
    if typeWidget == "widgettext":

        widgetTextForm = WidgetTextForm(request.POST or None)
        if widgetTextForm.is_valid():
            widgetText = widgetTextForm.save()

        widget = Widget.objects.create(
            content_object=widgetText,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetonlytext":

        widgetOnlyTextForm = WidgetOnlyTextForm(request.POST or None)

        if widgetOnlyTextForm.is_valid():
            widgetText = widgetOnlyTextForm.save()

        widget = Widget.objects.create(
            content_object=widgetText,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetphoto":
        
        widgetPhotoForm = WidgetPhotoForm(request.POST or None,request.FILES or None)
        if widgetPhotoForm.is_valid():
            widgetPhoto = widgetPhotoForm.save()
        
        widget = Widget.objects.create(
            content_object=widgetPhoto,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetgallery":
        
        widgetGallery = WidgetGalery.objects.create(
            title = request.POST.get('title')
        )
        widgetGallery.save()


        for image in request.FILES.getlist('images'):
            
            widgetGalleryPhoto = WidgetGalleryPhotos.objects.create(
                image=image,
                widgetGalery=widgetGallery
            )
            widgetGalleryPhoto.save()

        widget = Widget.objects.create(
            content_object=widgetGallery,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    
    return redirect(str(reverse('pageDetailView',  kwargs = {'pk' : page, })))