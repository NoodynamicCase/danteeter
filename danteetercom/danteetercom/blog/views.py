from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Blog
from blog.forms import BlogForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from .forms import BlogForm

# ===== LIST VIEW ============================================================
class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name="blog/listview.html"
    queryset = Blog.objects.order_by('-timestamp_added')


# == DETAIL VIEW ============================================================
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/detailview.html"
    queryset = Blog.objects.all()


# == UPDATE VIEW ============================================================
class BlogCreateView(LoginRequiredMixin, CreateView):
	form_class = BlogForm
	template_name = 'blog/createview.html'
	def get_queryset(self):
		return Blog.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(BlogCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(BlogCreateView, self).get_context_data(*args, **kwargs)
		context['Blog'] = "Create Blog Post"
		return context


# == UPDATE VIEW ============================================================
class BlogUpdateView(LoginRequiredMixin, UpdateView):
	form_class = BlogForm
	template_name="blog/updateview.html"
	def get_queryset(self):
		return Blog.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(BlogUpdateView, self).form_valid(form)


# ===== DELETE VIEW ====================================================
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)
    success_url = reverse_lazy('blog:listview')
