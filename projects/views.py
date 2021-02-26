from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    # Query to retrieve all objects in the projects table
    # Queryset = query
    projects = Project.objects.all()
    # A context dict to send info to our template for our project_index function
    context = {'projects': projects}
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    # Query to retrieve the project with primary key equal to pk's value
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)
