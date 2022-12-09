from django.shortcuts import render
from .models import Government, Employees


def list_employees_view(request):
    employees = Employees.objects.all()

    data = {
        'type': 1,
        'name': 'Преподаватели',
        'employees': employees,
    }
    return render(request, 'instructor/list.html', data)


def list_government_view(request):
    government = Government.objects.order_by('order').all()
    data = {
        'type': 2,
        'name': 'Руководители',
        'employees': government,
    }
    return render(request, 'instructor/list.html', data)


def employees_detail_view(request, pk, type):
    if type == 1:
        data_detail = Employees.objects.get(id=pk)
    else:
        data_detail = Government.objects.get(id=pk)

    data = {
        'type': type,
        'object': data_detail,
    }
    return render(request, 'instructor/detail.html', data)
