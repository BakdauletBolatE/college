from django.shortcuts import render, redirect
from .forms import AppForm
from django.contrib import messages
from .models import App,EduProgram
def main(request):

    form = AppForm()
    content = {
        "form": form
    }
    return render(request, 'registrationTemplate/main.html', content)

def dataView(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Файлы были успешно загружены')
            return redirect('/req/')
        else:
            print(form)
            print(form.errors)
            messages.error(request, 'Форма неверно заполнена ')
            return redirect('/req/')

    return render(request, 'registrationTemplate/main.html')
