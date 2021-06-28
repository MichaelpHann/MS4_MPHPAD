from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectCategory
from .forms import ProjectForm


def portfolio(request):
    """
    A view to show all portfolio projects
    """

    projects = Project.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            projects = projects.filter(category__name__in=categories)
            categories = ProjectCategory.objects.filter(name__in=categories)

    context = {
        'projects': projects,
        'current_categories': categories,
    }

    return render(request, 'portfolio/portfolio.html', context)


@login_required
def add_project(request):
    """
    A view to add a new portfolio project
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project added successfully!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'Failed to add project.\
                #  Please ensure the form is valid')
    else:
        form = ProjectForm()

    form = ProjectForm()
    template = 'portfolio/add_project.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_project(request, project_id):
    """
    A view to edit a portfolio project
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated project!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'Failed to update project. \
                # Please ensure the form is valid.')
    else:
        form = ProjectForm(instance=project)
        messages.info(request, f'You are editing {project.name}')

    template = 'portfolio/edit_project.html'
    context = {
        'form': form,
        'project': project,
    }

    return render(request, template, context)


@login_required
def delete_project(request, project_id):
    """
    A view to delete a project from the portfolio
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('portfolio'))
