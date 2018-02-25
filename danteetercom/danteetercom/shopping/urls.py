from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

app_name = 'shopping'

urlpatterns = [
    path('', views.ShoppingListView.as_view(), name='listview'),
    path('<int:pk>/', views.ShoppingDetailView.as_view(), name='detailview'),
    path('new/', views.ShoppingCreateView.as_view(), name='createview'),
    path('<int:pk>/edit/', views.ShoppingUpdateView.as_view(), name='updateview'),
    path('<int:pk>/delete/', views.ShoppingDeleteView.as_view(), name='deleteview'),

    # OTHERS
    path('grocery_list/', views.ShoppingGroceryListView.as_view(), name='grocery_listview'),
    path('store_list/', views.ShoppingStoreListView.as_view(), name='store_listview'),
    path('clothing_list/', views.ShoppingClothingListView.as_view(), name='clothing_listview'),
    path('ordered/', views.ShoppingOrderedListView.as_view(), name='ordered_listview'),
    path('wishlist/', views.ShoppingWishListListView.as_view(), name='wishlist_listview'),
    path('favorites/', views.ShoppingFavoritesListView.as_view(), name='favorites_listview'),
    path('archive/', views.ShoppingArchiveListView.as_view(), name='archive_listview'),

    ]
