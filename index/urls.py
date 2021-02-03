from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_home'),
    path('fighter/<int:pk>/', views.fighter, name='fighter'),
    path('info/', views.info, name='info'),
    path('round/', views.round, name='round'),
    path('lost/', views.lost, name='lost'),
]
