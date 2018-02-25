from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactsListView.as_view(), name='listview'),
    path('<int:pk>/', views.ContactsDetailView.as_view(), name='detailview'),
    path('new/', views.ContactsCreateView.as_view(), name='createview'),
    path('<int:pk>/edit/', views.ContactsUpdateView.as_view(), name='updateview'),
    path('<int:pk>/delete/', views.ContactsDeleteView.as_view(), name='deleteview'),
    ]
