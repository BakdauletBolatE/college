from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Specialization, SubSection, Qualification
from .forms import SpecializationCommentForm
from django.http import HttpResponse
from django.contrib import messages
from .serializator import SubSectionsSerializer, QualificationSerializer, SpecializationSerializer
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.

class SubSectionView(APIView):

    def get(self, request):
        subsection = SubSection.objects.all()
        serializer = SubSectionsSerializer(subsection, many=True)
        return JsonResponse({'data': serializer.data})


class SubSectionDetailView(APIView):

    def get(self, request, id):
        subsection = SubSection.objects.filter(section_id=id)
        serializer = SubSectionsSerializer(subsection, many=True)
        return JsonResponse({'data': serializer.data})


class SpecializationDetailView(APIView):

    def get(self, request, id):
        specialization = Specialization.objects.filter(subsection_id=id)
        serializer = SpecializationSerializer(specialization, many=True)
        return JsonResponse({'data': serializer.data})


class QualificationDetailView(APIView):

    def get(self, request, id):
        specialization = Qualification.objects.filter(specialization_id=id)
        serializer = QualificationSerializer(specialization, many=True)
        return JsonResponse({'data': serializer.data})


def index(request):
    specializations = Specialization.objects.all()
    data = {
        'specializations': specializations
    }

    return render(request, 'specialities/index.html', data)


def detail(request, pk):
    specialization = Specialization.objects.get(id=pk)
    comments = specialization.comments.filter(visible=True)
    form = SpecializationCommentForm()
    if request.method == "POST":
        form = SpecializationCommentForm(request.POST or None)

        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.author = request.user
            update_form.specialization = specialization
            update_form.save()
            messages.warning(request, 'Ваш отзыв ожидает модераций: Спасибо за отклик')  # ignored

            return redirect(str(reverse('specapp:detail', args=[pk])) + "#review")

    data = {
        'form': form,
        'comments': comments,
        'specialization': specialization
    }

    return render(request, 'specialization/single-page.html', data)
