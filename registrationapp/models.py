from django.db import models
from docxtpl import DocxTemplate
from django.conf import settings
from specializationapp.models import Specialization

class EduProgram(models.Model):
    name = models.CharField('Образовательная программа', max_length=255)

    class Meta:
        verbose_name = "Образовательную программу"
        verbose_name_plural = "Образовательные программы"

    def __str__(self):
        return self.name

class App(models.Model):

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

    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    otch = models.CharField('Отчество', max_length=255, null=True, blank=True, default="")
    phone = models.CharField('Номер телефона', max_length=11)
    edu_program = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Образовательная программа')
    language = models.CharField('Язык обучения', choices=lang, max_length=255)
    finish_edu = models.TextField("Прежнее место обучение и дата окончания", null=True, blank=True)
    address = models.CharField("Адрес проживания", max_length=255)
    place = models.BooleanField("Общежитие" ,default=False)
    about = models.TextField("Информация о себе", null=True, blank=True)
    gender = models.CharField("Пол", choices=gend, max_length=255)
    birthday = models.DateField("Дата рождения",auto_now_add=False, blank=True, null=True)
    born_place = models.CharField("Место рождения", max_length=255)
    national = models.CharField("Нация", max_length=255)
    polojenie = models.CharField("Материальное положение", max_length=255, choices=poloj)
    information_parent_mom = models.TextField("ФИО матери, место проживания, номер телефона", null=True, blank=True)
    information_parent_dad = models.TextField("ФИО отца, место проживания, номер телефона", null=True, blank=True)
    created_at = models.DateField(auto_now_add=False, null=True, blank=True)

    id_card_front = models.FileField('Уд.лич лицевая', upload_to='id_card/', null=True, blank=True)
    id_card_back = models.FileField('Уд.лич обратная', upload_to='id_card/', null=True, blank=True)
    diplom = models.FileField('Диплом', upload_to='diplom/')
    zayavka = models.FileField('Заявка для приема на учебу', upload_to='zayavka/')
    fluro = models.FileField("075-y(флюрография)", upload_to="fluro/")
    zdorovie = models.FileField("063-y(Паспорт о здоровье)", upload_to="zdorovie/")
    photo = models.FileField("3x4 фото", upload_to="photo/")
    genereted_file = models.FileField(upload_to="genereted/", null=True, blank=True)


    def __str__(self):
        return f'{self.surname} {self.name}'

    def save(self, *args, **kwargs):
        doc = DocxTemplate("template_form.docx")
        if self.place:
            place = "Керек"
        else:
            place = "Керек емес"
        context = {
            'fio': f'{self.surname} {self.name} {self.otch}',
            'finish_edu': self.finish_edu,
            'address': self.address,
            'place': place,
            'edu': self.edu_program,
            'about_me': self.about,
            'gender': self.gender,
            'birthday': self.birthday,
            'born_place': self.born_place,
            'national': self.national,
            'pol': self.polojenie,
            'inf_mom': self.information_parent_mom,
            'inf_dad': self.information_parent_dad,
            'about': self.about,
            'created': self.created_at
        }
        doc.render(context)
        name = f"/genereted/{self.name}_{self.surname}_request.docx"
        print(settings.MEDIA_ROOT)
        doc.save(str(settings.MEDIA_ROOT)+name)
        self.genereted_file = name
        super(App, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заявку"
        verbose_name_plural = "Заявки"

# # окуга кабылдау туралы отиниш
# # билим туралы кужат
# # 075-у нысаны бойынша медициналык аныктама(флюрография)
# # 063-у нысаны бойынша медициналык (денсаулык паспорты)
# # туу туралы куалигин немесе жеке куалигинин коширмеси
# 3х4 фото