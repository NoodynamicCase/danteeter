from django.contrib.auth.decorators import login_required
from django.db.models import Q #"Called Q Lookups"
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Contacts
from contacts.forms import ContactsForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from .forms import ContactsForm

# ===== LIST VIEW ============================================================
class ContactsListView(LoginRequiredMixin, ListView):
    model = Contacts
    template_name="contacts/listview.html"
    queryset = Contacts.objects.order_by('connection_type','last_name')


# == DETAIL VIEW ============================================================
class ContactsDetailView(LoginRequiredMixin, DetailView):
    model = Contacts
    template_name = "contacts/detailview.html"
    queryset = Contacts.objects.all()


# == UPDATE VIEW ============================================================
class ContactsCreateView(LoginRequiredMixin, CreateView):
	form_class = ContactsForm
	template_name = 'contacts/createview.html'
	def get_queryset(self):
		return Contacts.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ContactsCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(ContactsCreateView, self).get_context_data(*args, **kwargs)
		context['Contacts'] = "Create Contact"
		return context


# == UPDATE VIEW ============================================================
class ContactsUpdateView(LoginRequiredMixin, UpdateView):
	form_class = ContactsForm
	template_name="contacts/updateview.html"
	def get_queryset(self):
		return Contacts.objects.filter(user=self.request.user)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(ContactsUpdateView, self).form_valid(form)


# ===== DELETE VIEW ====================================================
class ContactsDeleteView(LoginRequiredMixin, DeleteView):
    model = Contacts
    template_name = "contacts/contacts_confirm_delete.html"
    def get_queryset(self):
        return Contacts.objects.filter(user=self.request.user)
    success_url = reverse_lazy('contacts:listview')
