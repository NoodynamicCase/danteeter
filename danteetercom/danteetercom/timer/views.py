from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Timer
from timer.forms import TimerForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from crispy_forms.helper import FormHelper
from .forms import TimerForm

class TimerFormView(FormView):
    template_name = 'timer/createview.html'
    form_class = TimerForm
    # success_url="/timer/%s/edit" % (10)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        # success_url="/timer/%s/edit" % (form.id)
        return super().form_valid(form)
        # return redirect(success_url)

# ===== LIST VIEW ============================================================
class TimerListView(LoginRequiredMixin, ListView):
    model = Timer
    template_name="timer/listview.html"
    queryset = Timer.objects.order_by('-stop_time')


# == DETAIL VIEW ============================================================
class TimerDetailView(LoginRequiredMixin, DetailView):
    model = Timer
    template_name = "timer/detailview.html"
    queryset = Timer.objects.all()


# == CREATE VIEW ============================================================
class TimerCreateView(LoginRequiredMixin, CreateView):
	form_class = TimerForm
	template_name = 'timer/createview.html'

	def get_queryset(self):
		return Timer.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(TimerCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(TimerCreateView, self).get_context_data(*args, **kwargs)
		context['Timer'] = "Create Item"
		return context



# == UPDATE VIEW ============================================================
class TimerUpdateView(LoginRequiredMixin, UpdateView):
	form_class = TimerForm
	template_name="timer/updateview.html"
	def get_queryset(self):
		return Timer.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(TimerUpdateView, self).form_valid(form)



# ===== DELETE VIEW ====================================================
class TimerDeleteView(LoginRequiredMixin, DeleteView):
    model = Timer
    template_name = "timer/timer_confirm_delete.html"
    def get_queryset(self):
        return Timer.objects.filter(user=self.request.user)
    success_url = reverse_lazy('timer:listview')
