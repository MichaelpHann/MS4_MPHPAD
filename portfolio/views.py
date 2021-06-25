from django.shortcuts import render
from .models import Project


def portfolio(request):
    """
    A view to return the index/homepage
    """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)
    