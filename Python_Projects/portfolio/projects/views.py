from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views import View

from projects.models import Project


class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request, "projects/projects_index.html", context)


class ProjectDetailView(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        context = {
            'project': project
        }
        return render(request, 'projects/project_detail.html',context)

