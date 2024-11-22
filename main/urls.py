from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search),
    path('gallery', views.gallery),
    path('news', views.news),
    path('about', views.about),
    path('login', views.login_def),
    path('logout', views.log_out),
    path('profile', views.profile)
]
