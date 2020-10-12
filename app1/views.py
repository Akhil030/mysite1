from django.shortcuts import render
from .models import Projects


def projects(request):
    proj = Projects.objects.all()

    return render(request, "projects.html", {"projects": proj})
