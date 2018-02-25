from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Shopping
from shopping.forms import ShoppingForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from .forms import ShoppingForm

# ===== LIST VIEW ============================================================
class ShoppingListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/listview.html"
    queryset = Shopping.objects.order_by('-timestamp_added')

class ShoppingGroceryListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/grocery_listview.html"
    queryset = Shopping.objects.filter(store='Grocery').exclude(in_list=False).exclude(ordered=True)

class ShoppingStoreListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/store_listview.html"
    queryset = Shopping.objects.filter(store='Other').exclude(in_list=False).exclude(ordered=True)

class ShoppingClothingListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/clothing_listview.html"
    queryset = Shopping.objects.filter(item_category='Clothing').exclude(in_list=False).exclude(ordered=True)

class ShoppingOrderedListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/ordered_listview.html"
    queryset = Shopping.objects.filter(ordered=True).exclude(in_list=False)

class ShoppingWishListListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/wishlist_listview.html"
    queryset = Shopping.objects.filter(wish_list=True)

class ShoppingFavoritesListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/favorites_listview.html"
    queryset = Shopping.objects.filter(favorite=True)

class ShoppingArchiveListView(LoginRequiredMixin, ListView):
    model = Shopping
    template_name="shopping/additional/archive_listview.html"
    queryset = Shopping.objects.filter(in_list=False)

# == DETAIL VIEW ============================================================
class ShoppingDetailView(LoginRequiredMixin, DetailView):
    model = Shopping
    template_name = "shopping/detailview.html"
    queryset = Shopping.objects.all()


# == UPDATE VIEW ============================================================
class ShoppingCreateView(LoginRequiredMixin, CreateView):
	form_class = ShoppingForm
	template_name = 'shopping/createview.html'

	def get_queryset(self):
		return Shopping.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ShoppingCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(ShoppingCreateView, self).get_context_data(*args, **kwargs)
		context['Shopping'] = "Create Item"
		return context

# == UPDATE VIEW ============================================================
class ShoppingUpdateView(LoginRequiredMixin, UpdateView):
	form_class = ShoppingForm
	template_name="shopping/updateview.html"
	def get_queryset(self):
		return Shopping.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ShoppingUpdateView, self).form_valid(form)


# ===== DELETE VIEW ====================================================
class ShoppingDeleteView(LoginRequiredMixin, DeleteView):
    model = Shopping
    template_name = "shopping/shopping_confirm_delete.html"
    def get_queryset(self):
        return Shopping.objects.filter(user=self.request.user)
    success_url = reverse_lazy('shopping:listview')
