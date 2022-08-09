from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('new-process/',views.new_process, name='new-process'),
    path('schedule-project/<str:pk>',views.schedule_project, name='schedule-project'),

]
