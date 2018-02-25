from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'humancapital'

urlpatterns = [
    # path('', views.HumanCapitalPostListView.as_view(), name='home'),

    # POSTS
    path('posts/', views.HumanCapitalPostListView.as_view(), name='posts_listview'),
    path('posts/<int:pk>/', views.HumanCapitalPostDetailView.as_view(), name='posts_detailview'),
    path('posts/new/', views.HumanCapitalPostCreateView.as_view(), name='posts_createview'),
    path('posts/<int:pk>/edit/', views.HumanCapitalPostUpdateView.as_view(), name='posts_updateview'),
    path('posts/<int:pk>/delete/', views.HumanCapitalPostDeleteView.as_view(), name='posts_deleteview'),

    # JARGON
    path('jargon/', views.HumanCapitalJargonListView.as_view(), name='jargon_listview'),
    path('jargon/<int:pk>/', views.HumanCapitalJargonDetailView.as_view(), name='jargon_detailview'),
    path('jargon/new/', views.HumanCapitalJargonCreateView.as_view(), name='jargon_createview'),
    path('jargon/<int:pk>/edit/', views.HumanCapitalJargonUpdateView.as_view(), name='jargon_updateview'),
    path('jargon/<int:pk>/delete/', views.HumanCapitalJargonDeleteView.as_view(), name='jargon_deleteview'),

    # JARGON
    path('sources/', views.HumanCapitalSourceListView.as_view(), name='sources_listview'),
    path('sources/<int:pk>/', views.HumanCapitalSourceDetailView.as_view(), name='sources_detailview'),
    path('sources/new/', views.HumanCapitalSourceCreateView.as_view(), name='sources_createview'),
    path('sources/<int:pk>/edit/', views.HumanCapitalSourceUpdateView.as_view(), name='sources_updateview'),
    path('sources/<int:pk>/delete/', views.HumanCapitalSourceDeleteView.as_view(), name='sources_deleteview'),

    ]
