from django import forms
from .models import *
from django.core.exceptions import ObjectDoesNotExist




class AddRateForm(forms.ModelForm):

    class Meta:

        model = Rating
        fields = ('__all__')

class AddAnswerForm(forms.ModelForm):

    class Meta:

        model = Answer
        fields = ('__all__')

class AddTaskForm(forms.ModelForm):

    class Meta:

        model = Tasks
        fields = ('__all__')
    


     

        