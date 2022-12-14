from .models import Page
from django import forms


class C(forms.ModelChoiceField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PageForm(forms.ModelForm):
    variants = Page.objects.all()

    products = [('a', 'a') for i in variants]

    parent = forms.ChoiceField(choices=products)

    class Meta:
        model = Page
        fields = '__all__'
