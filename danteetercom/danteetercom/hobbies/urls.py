from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'hobbies'

urlpatterns = [
    # path('', views.HobbiesListView.as_view(), name='home'),

# COOKING
    path('cooking/', views.CookingListView.as_view(), name='cooking_listview'),
    path('cooking/<int:pk>/', views.CookingDetailView.as_view(), name='cooking_detailview'),
    path('cooking/new/', views.CookingCreateView.as_view(), name='cooking_createview'),
    path('cooking/<int:pk>/edit/', views.CookingUpdateView.as_view(), name='cooking_updateview'),
    path('cooking/<int:pk>/delete/', views.CookingDeleteView.as_view(), name='cooking_deleteview'),

# GUITAR
    path('guitar/', views.GuitarListView.as_view(), name='guitar_listview'),
    path('guitar/<int:pk>/', views.GuitarDetailView.as_view(), name='guitar_detailview'),
    path('guitar/new/', views.GuitarCreateView.as_view(), name='guitar_createview'),
    path('guitar/<int:pk>/edit/', views.GuitarUpdateView.as_view(), name='guitar_updateview'),
    path('guitar/<int:pk>/delete/', views.GuitarDeleteView.as_view(), name='guitar_deleteview'),
    ]
