from .models import Page, PageCategory
from django import forms
from .models import Widget, WidgetText,WidgetPhoto,WidgetOnlyText



class PageForm(forms.ModelForm):


    class Meta:

        model = Page
        fields = ['title','title_kk','title_en','url','slug','link','category']
        widgets = {
                'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'title_en': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'title_kk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'slug нужно написать адресс без пробелов на латинском'
                }),
                'url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'по умолчанию нужно писать обязательно pageView',
                'value':'sapp:pageView'
                }),
                'link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'если нужно просто оставить ссылку на другие сайты (http://example.com)'
                }),
                'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
                }),
                
            }

class PageCategoryForm(forms.ModelForm):


    class Meta:

        model = PageCategory
        fields = ['name','name_kk','name_en','linkto']
        widgets = {
                'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'name_kk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'name_en': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите названия страницы',
                }),
                'linkto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'если нужно просто оставить ссылку на другие сайты (http://example.com)'
                }),     
            }

class WidgetForm(forms.ModelForm):

    class Meta:

        model = Widget
        fields = ('__all__')

class WidgetTextForm(forms.ModelForm):

    class Meta:
        model = WidgetText
        fields = ('__all__')

class WidgetOnlyTextForm(forms.ModelForm):

    class Meta:
        model = WidgetOnlyText
        fields = ('__all__')

class WidgetPhotoForm(forms.ModelForm):

    class Meta:
        model = WidgetPhoto
        fields = ('__all__')

