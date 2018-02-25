from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import HumanCapitalPost, HumanCapitalJargon, HumanCapitalSource
from humancapital.forms import HumanCapitalPostForm, HumanCapitalJargonForm, HumanCapitalSourceForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper

# ===== LIST VIEW ============================================================
class HumanCapitalPostListView(LoginRequiredMixin, ListView):
    model = HumanCapitalPost
    template_name="humancapital/posts/listview.html"
    queryset = HumanCapitalPost.objects.order_by('-timestamp_updated')

# == DETAIL VIEW ============================================================
class HumanCapitalPostDetailView(LoginRequiredMixin, DetailView):
    model = HumanCapitalPost
    template_name = "humancapital/posts/detailview.html"
    queryset = HumanCapitalPost.objects.all()

# == UPDATE VIEW ============================================================
class HumanCapitalPostCreateView(LoginRequiredMixin, CreateView):
	form_class = HumanCapitalPostForm
	template_name = 'humancapital/posts/createview.html'
	def get_queryset(self):
		return HumanCapitalPost.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalPostCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(HumanCapitalPostCreateView, self).get_context_data(*args, **kwargs)
		context['HumanCapitalPost'] = "Create HC Post"
		return context

# == UPDATE VIEW ============================================================
class HumanCapitalPostUpdateView(LoginRequiredMixin, UpdateView):
	form_class = HumanCapitalPostForm
	template_name="humancapital/posts/updateview.html"
	def get_queryset(self):
		return HumanCapitalPost.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalPostUpdateView, self).form_valid(form)

# ===== DELETE VIEW ====================================================
class HumanCapitalPostDeleteView(LoginRequiredMixin, DeleteView):
    model = HumanCapitalPost
    template_name = "humancapital/posts/humancapital_confirm_delete.html"
    def get_queryset(self):
        return HumanCapitalPost.objects.filter(user=self.request.user)
    success_url = reverse_lazy('humancapital:posts_listview')



# ==================== JARGON ====================================================


# ===== LIST VIEW ============================================================
class HumanCapitalJargonListView(LoginRequiredMixin, ListView):
    model = HumanCapitalJargon
    template_name="humancapital/jargon/listview.html"
    queryset = HumanCapitalJargon.objects.order_by('-timestamp_updated')

# == DETAIL VIEW ============================================================
class HumanCapitalJargonDetailView(LoginRequiredMixin, DetailView):
    model = HumanCapitalJargon
    template_name = "humancapital/jargon/detailview.html"
    queryset = HumanCapitalJargon.objects.all()

# == UPDATE VIEW ============================================================
class HumanCapitalJargonCreateView(LoginRequiredMixin, CreateView):
	form_class = HumanCapitalJargonForm
	template_name = 'humancapital/jargon/createview.html'
	def get_queryset(self):
		return HumanCapitalJargon.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalJargonCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(HumanCapitalJargonCreateView, self).get_context_data(*args, **kwargs)
		context['HumanCapitalJargon'] = "Create Jargon Term"
		return context

# == UPDATE VIEW ============================================================
class HumanCapitalJargonUpdateView(LoginRequiredMixin, UpdateView):
	form_class = HumanCapitalJargonForm
	template_name="humancapital/jargon/updateview.html"
	def get_queryset(self):
		return HumanCapitalJargon.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalJargonUpdateView, self).form_valid(form)

# ===== DELETE VIEW ====================================================
class HumanCapitalJargonDeleteView(LoginRequiredMixin, DeleteView):
    model = HumanCapitalJargon
    template_name = "humancapital/jargon/humancapital_confirm_delete.html"
    def get_queryset(self):
        return HumanCapitalJargon.objects.filter(user=self.request.user)
    success_url = reverse_lazy('humancapital:jargon_listview')



# ==================== SOURCES =================================================


# ===== LIST VIEW ============================================================
class HumanCapitalSourceListView(LoginRequiredMixin, ListView):
    model = HumanCapitalSource
    template_name="humancapital/sources/listview.html"
    queryset = HumanCapitalSource.objects.order_by('-timestamp_updated')

# == DETAIL VIEW ============================================================
class HumanCapitalSourceDetailView(LoginRequiredMixin, DetailView):
    model = HumanCapitalSource
    template_name = "humancapital/sources/detailview.html"
    queryset = HumanCapitalSource.objects.all()

# == UPDATE VIEW ============================================================
class HumanCapitalSourceCreateView(LoginRequiredMixin, CreateView):
	form_class = HumanCapitalSourceForm
	template_name = 'humancapital/sources/createview.html'
	def get_queryset(self):
		return HumanCapitalSource.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalSourceCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(HumanCapitalSourceCreateView, self).get_context_data(*args, **kwargs)
		context['HumanCapitalSource'] = "Create Source Term"
		return context

# == UPDATE VIEW ============================================================
class HumanCapitalSourceUpdateView(LoginRequiredMixin, UpdateView):
	form_class = HumanCapitalSourceForm
	template_name="humancapital/sources/updateview.html"
	def get_queryset(self):
		return HumanCapitalSource.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(HumanCapitalSourceUpdateView, self).form_valid(form)

# ===== DELETE VIEW ====================================================
class HumanCapitalSourceDeleteView(LoginRequiredMixin, DeleteView):
    model = HumanCapitalSource
    template_name = "humancapital/sources/humancapital_confirm_delete.html"
    def get_queryset(self):
        return HumanCapitalSource.objects.filter(user=self.request.user)
    success_url = reverse_lazy('humancapital:sources_listview')
