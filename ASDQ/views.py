from django.shortcuts import render
from .models import Run, Users
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def run_view(request):
    run_list = Run.objects.all()
    return render(request, 'home.html', {'run_list': run_list})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserUpdateView(UpdateView):
    model = Users
    fields = ('country', 'discord', 'twitter', 'twitch')
    template_name = 'change.html'
    success_url = reverse_lazy('user')


class UserDeleteView(DeleteView):
    model = Users
    template_name = 'user_delete.html'
    success_url = reverse_lazy('')


def accountview(request):
    # user = request.user
    return render(request, 'user.html')


class RunSubmission(LoginRequiredMixin,CreateView):
    model = Run
    template_name = 'submit.html'
    fields = ('date', 'time', 'status', 'game_ID', 'platform')
    login_url = 'login'


class RunConfirmation(LoginRequiredMixin, UpdateView):
    model = Run
    template_name = 'confirm.html'
    fields = 'status'
    login_url = 'login'

