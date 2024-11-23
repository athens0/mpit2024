from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('analytics', views.analytics),
    path('analytics/<int:month>', views.analytics),
    path('teams', views.teams),
    path('matches', views.matches),
    path('login', views.login_def),
    path('logout', views.log_out),
    path('profile', views.profile)
]
