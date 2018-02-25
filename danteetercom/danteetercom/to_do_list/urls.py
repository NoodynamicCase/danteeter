from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'to_do_list'

urlpatterns = [
# TO DO LIST
    path('', views.To_Do_ListListView.as_view(), name='tasks_listview'),
    path('tasks/', views.To_Do_ListListView.as_view(), name='tasks_listview'),
    path('tasks/<int:pk>/', views.To_Do_ListDetailView.as_view(), name='tasks_detailview'),
    path('tasks/new/', views.To_Do_ListCreateView.as_view(), name='tasks_createview'),
    path('tasks/<int:pk>/edit/', views.To_Do_ListUpdateView.as_view(), name='tasks_updateview'),
    path('tasks/<int:pk>/delete/', views.To_Do_ListDeleteView.as_view(), name='tasks_deleteview'),
# DAILY LOG
    path('dailylog/', views.DailyLogListView.as_view(), name='dailylog_listview'),
    path('dailylog/<int:pk>/', views.DailyLogDetailView.as_view(), name='dailylog_detailview'),
    path('dailylog/new/', views.DailyLogCreateView.as_view(), name='dailylog_createview'),
    path('dailylog/<int:pk>/edit/', views.DailyLogUpdateView.as_view(), name='dailylog_updateview'),
    path('dailylog/<int:pk>/delete/', views.DailyLogDeleteView.as_view(), name='dailylog_deleteview'),
    ]
