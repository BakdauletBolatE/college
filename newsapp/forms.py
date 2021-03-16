from django import forms
from .models import NewsComment

class NewsCommentForm(forms.ModelForm):

    class Meta:

        fields = ('text',)
        model = NewsComment
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'