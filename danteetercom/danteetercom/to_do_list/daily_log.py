from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import DailyLog
from to_do_list.forms import DailyLogForm, DailyLog_FileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from .forms import DailyLogForm

# ===== LIST VIEW ============================================================
class DailyLogListView(LoginRequiredMixin, ListView):
    model = DailyLog
    template_name="DailyLog/listview.html"
    queryset = DailyLog.objects.exclude(task_archive=True).order_by('-timestamp_added')


# == DETAIL VIEW ============================================================
class DailyLogDetailView(LoginRequiredMixin, DetailView):
    model = DailyLog
    template_name = "to_do_list/detailview.html"
    queryset = DailyLog.objects.all()


# == UPDATE VIEW ============================================================
class DailyLogCreateView(LoginRequiredMixin, CreateView):
	form_class = DailyLogForm
	template_name = 'to_do_list/createview.html'

	def get_queryset(self):
		return DailyLog.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(DailyLogCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(DailyLogCreateView, self).get_context_data(*args, **kwargs)
		context['DailyLog'] = "Create Item"
		return context

# == UPDATE VIEW ============================================================
class DailyLogUpdateView(LoginRequiredMixin, UpdateView):
	form_class = DailyLogForm
	template_name="to_do_list/updateview.html"
	def get_queryset(self):
		return DailyLog.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(DailyLogUpdateView, self).form_valid(form)


# ===== DELETE VIEW ====================================================
class DailyLogDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyLog
    template_name = "to_do_list/to_do_list_confirm_delete.html"
    def get_queryset(self):
        return DailyLog.objects.filter(user=self.request.user)
    success_url = reverse_lazy('to_do_list:listview')