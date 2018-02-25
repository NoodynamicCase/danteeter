from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='listview'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detailview'),
    path('new/', views.BlogCreateView.as_view(), name='createview'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='updateview'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='deleteview'),
    ]
