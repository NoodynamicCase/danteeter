from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'timer'

urlpatterns = [
    path('', views.TimerListView.as_view(), name='listview'),
    path('<int:pk>/', views.TimerDetailView.as_view(), name='detailview'),
    path('new/', views.TimerCreateView.as_view(), name='createview'),
    path('formview/', views.TimerFormView.as_view(), name='formview'),
    path('<int:pk>/edit/', views.TimerUpdateView.as_view(), name='updateview'),
    path('<int:pk>/delete/', views.TimerDeleteView.as_view(), name='deleteview'),
    ]
