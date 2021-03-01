from django import forms
from django.forms import ModelForm
from .models import Run, Users, Game
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required


# for datetime
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


# for Date
class DateInput(forms.DateInput):
    input_type = 'date'


# for Time
class TimeInput(forms.TimeInput):
    input_type = 'time'


class UserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Users
        fields = ('user', 'country', 'discord', 'twitter', 'twitch')


class UserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('country', 'discord', 'twitter', 'twitch')


class RunSubmission(ModelForm):
    class Meta:
        model = Run
        fields = ['date', 'time', 'game_ID', ]

    @login_required
    def ask(request):
        form = RunSubmission(request.POST)

        if form.is_valid():
            runner = form.save(False)
            runner.user = request.user
            runner.save()
