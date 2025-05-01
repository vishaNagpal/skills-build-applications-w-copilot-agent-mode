from django.contrib import admin

from .models import User, Team, Activity, Leaderboard, Workout
from django.contrib import admin

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
