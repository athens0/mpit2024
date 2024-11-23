from django.contrib import admin
from .models import Match, Team, Prediction

# Register your models here.
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Prediction)