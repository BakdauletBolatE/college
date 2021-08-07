from django import forms
from .models import App
from specializationapp.models import Specialization

lang = (
        ('Русский', 'Русский'),
        ('Казахский', 'Казахский'),
    )

gend = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

poloj = (
        ('Ниже среднего', 'Ниже среднего'),
        ('Среднее', 'Среднее'),
        ('Высокое', 'Высокое'),
    )
class AppForm(forms.ModelForm):
    edu_program = forms.ModelChoiceField(queryset=Specialization.objects.all(), to_field_name="id",widget=forms.Select(attrs={'class': 'custom-select'}) )
    language = forms.ChoiceField(choices=lang, widget=forms.Select(attrs={'class': 'custom-select'}))
    gender = forms.ChoiceField(choices=gend, widget=forms.Select(attrs={'class': 'custom-select'}))
    polojenie = forms.ChoiceField(choices=poloj, widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = App
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше фамилия"}),
            'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше имя"}),
            'otch': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Ваше отчество"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', "placeholder": " +7"}),
            'finish_edu': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type':"date", 'class':"icon-date_range"}),
            'born_place': forms.TextInput(attrs={'class': 'form-control'}),
            'national': forms.TextInput(attrs={'class': 'form-control'}),
            'information_parent_mom': forms.Textarea(attrs={'class': 'form-control'}),
            'information_parent_dad': forms.Textarea(attrs={'class': 'form-control'}),
            'created_at': forms.DateInput(attrs={'type':"datetime-local", 'class':"icon-date_range"}),
            'id_card_front': forms.FileInput(attrs={'class': 'custom-file-input', "onChange":"updateValue(this, 'id_card_frontLabel')"}),
            'id_card_back': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Уд.лич обратная", "onChange":"updateValue(this, 'id_card_backLabel')"}),
            'diplom': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Диплом", "onChange":"updateValue(this, 'diplomLabel')"}),
            'zayavka': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Заявление на обучение", "onChange":"updateValue(this, 'zayavkaLabel')"}),
            'fluro': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Флюрография", "onChange":"updateValue(this, 'fluroLabel')"}),
            'zdorovie': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "Справка о здоровье", "onChange":"updateValue(this, 'zdorovieLabel')"}),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input', "placeholder": "3х4 фото", "onChange":"updateValue(this, '34photoSize')"}),
        }
        # finish_edu = models.TextField
        # address = models.CharField
        # place = models.BooleanField
        # about = models.TextField
        # gender = models.CharField
        # birthday = models.DateField
        # born_place = models.CharField
        # national = models.CharField
        # polojenie = models.CharField
        # information_parent_mom = models.TextField
        # information_parent_dad = models.TextField
        # created_at = models.DateField