from django.shortcuts import render
from . import models


def get_resumes(request):
    resumes = models.Resume.objects.all()
    return render(request, 'resumes.html', context={"resumes": resumes})
