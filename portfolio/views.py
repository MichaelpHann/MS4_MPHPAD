from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


def portfolio(request):
    """
    A view to return the index/homepage
    """

    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)


@login_required
def add_project(request):
    """
    A view to add a new portfolio project
    """
    if not request.user.is_superuser:
        # messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            # messages.success(request, 'Project added successfully!')
            return redirect(reverse('portfolio', args=[project.id]))
        # else:
            # messages.error(request, 'Failed to add project.\
                #  Please ensure the form is valid')
    else:
        form = ProjectForm()

    form = ProjectForm()
    template = 'portfolio/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
