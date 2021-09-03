from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.views import View



class ResumeView(View):

    def get(self, request):
        resumes = models.Resume.objects.all()
        return render(request, 'resumes.html', context={"resumes": resumes})

    def post(self, request):
        if request.user.is_authenticated:
            resume = models.Resume.objects.create(
                author=request.user,
                description=request.POST.get("description", "")
            )
            resume.save()
            return redirect("/resumes")
        else:
            return HttpResponse(status=403)

