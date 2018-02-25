from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Guitar, Cooking
from hobbies.forms import GuitarForm, CookingForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from .forms import GuitarForm


# ===== COOKING ============================================================
class CookingListView(LoginRequiredMixin, ListView):
    model = Cooking
    template_name="hobbies/cooking/listview.html"
    queryset = Cooking.objects.order_by('-timestamp_added')


# == DETAIL VIEW ===
class CookingDetailView(LoginRequiredMixin, DetailView):
    model = Cooking
    template_name = "hobbies/cooking/detailview.html"
    queryset = Cooking.objects.all()


# == UPDATE VIEW ===
class CookingCreateView(LoginRequiredMixin, CreateView):
	form_class = CookingForm
	template_name = 'hobbies/cooking/createview.html'

	def get_queryset(self):
		return Cooking.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(CookingCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(CookingCreateView, self).get_context_data(*args, **kwargs)
		context['Cooking'] = "Create Item"
		return context

# == UPDATE VIEW ==
class CookingUpdateView(LoginRequiredMixin, UpdateView):
	form_class = CookingForm
	template_name="hobbies/cooking/updateview.html"
	def get_queryset(self):
		return Cooking.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(CookingUpdateView, self).form_valid(form)


# ===== DELETE VIEW ===
class CookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Cooking
    template_name = "hobbies/cooking/hobbies_confirm_delete.html"
    def get_queryset(self):
        return Cooking.objects.filter(user=self.request.user)
    success_url = reverse_lazy('cooking:cooking_listview')




# ===== GUITAR ============================================================
class GuitarListView(LoginRequiredMixin, ListView):
    model = Guitar
    template_name="hobbies/guitar/listview.html"
    queryset = Guitar.objects.order_by('artist')


# == DETAIL VIEW ==
class GuitarDetailView(LoginRequiredMixin, DetailView):
    model = Guitar
    template_name = "hobbies/guitar/detailview.html"
    queryset = Guitar.objects.all()


# == UPDATE VIEW ===
class GuitarCreateView(LoginRequiredMixin, CreateView):
	form_class = GuitarForm
	template_name = 'hobbies/guitar/createview.html'

	def get_queryset(self):
		return Guitar.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(GuitarCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(GuitarCreateView, self).get_context_data(*args, **kwargs)
		context['Guitar'] = "Create Item"
		return context

# == UPDATE VIEW ==
class GuitarUpdateView(LoginRequiredMixin, UpdateView):
	form_class = GuitarForm
	template_name="hobbies/guitar/updateview.html"
	def get_queryset(self):
		return Guitar.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(GuitarUpdateView, self).form_valid(form)


# ===== DELETE VIEW ==
class GuitarDeleteView(LoginRequiredMixin, DeleteView):
    model = Guitar
    template_name = "hobbies/guitar/deleteview.html"
    def get_queryset(self):
        return Guitar.objects.filter(user=self.request.user)
    success_url = reverse_lazy('hobbies:guitar_listview')
