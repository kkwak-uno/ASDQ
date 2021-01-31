from django.contrib import admin
from .models import Game, Run, Users
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UsersInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (UsersInline,)
    list_display = ('username', 'email', 'country', 'discord', 'twitter', 'twitch')

    def country(self, obj):
        return Users.objects.get(user=obj).country
    def discord(self, obj):
        return Users.objects.get(user=obj).discord
    def twitter(self, obj):
        return Users.objects.get(user=obj).twitter
    def twitch(self, obj):
        return Users.objects.get(user=obj).twitch



class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ('title', 'release_date', 'platform')
    list_filter = ('title', 'release_date', 'platform')
    ordering = ['title']


class RunAdmin(admin.ModelAdmin):
    model = Run
    list_display = ('user', 'date', 'time', 'game_ID', 'status')


admin.site.register(Game, GameAdmin)
admin.site.register(Run, RunAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)