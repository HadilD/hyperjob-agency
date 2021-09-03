from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.http import HttpResponse


class VacancyView(View):

    def get(self, request):
        vacancies = models.Vacancy.objects.all()
        return render(request, "vacancy/vacancies.html", context={'vacancies': vacancies})


    def post(self, request):
        if request.user.is_staff:
            vacancy = models.Vacancy.objects.create(
                author=request.user,
                description=request.POST.get("description", "")
            )
            vacancy.save()
            return redirect("/vacancies")
        else:
            return HttpResponse(status=403)
