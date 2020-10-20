from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.enter, name='enter'),
    path('health/', views.health, name='health'),
    path('science/', views.science, name='science'),
    path('sports/', views.sports, name='sports'),
    path('tech/', views.tech, name='tech'),
]