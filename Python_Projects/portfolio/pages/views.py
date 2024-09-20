from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'home.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
