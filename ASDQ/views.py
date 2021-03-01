from django.shortcuts import render
from .models import Run
from django.views.generic import TemplateView, ListView


def run_view(request):
    run_list = Run.objects.all()
    return render(request, 'home.html', {'run_list': run_list})
