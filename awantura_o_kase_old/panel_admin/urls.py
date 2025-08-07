from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login, name = 'login'),
    path('panel/', views.panel, name = 'panel'),
    path('gra/', views.gra, name = 'gra'),
    path('viewers/', views.viewers, name = 'viewers'),
    path('niebiescy/', views.niebiescy_viewers, name = 'niebiescy'),
    path('zolci/', views.zolci_viewers, name = 'zolci'),
    path('zieloni/', views.zieloni_viewers, name = 'zieloni'),
    path('mistrzowie/', views.mistrzowie_viewers, name = 'mistrzowie'),
    path('stream_panel/', views.stream_panel, name = 'stream_panel'),
]
