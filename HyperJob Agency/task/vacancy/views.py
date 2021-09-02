from django.shortcuts import render
from . import models


def get_vacancies(request):
    vacancies = models.Vacancy.objects.all()
    return render(request, "vacancy/vacancies.html", context={'vacancies': vacancies})