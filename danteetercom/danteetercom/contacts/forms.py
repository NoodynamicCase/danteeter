from django import forms
from .models import Contacts
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = [
            'new',
            'first_name',
            'last_name',
            'email',
            'phone',
            'quick_reference',
            'notes',
            'connection_type',
            'connection_quality',
            'file_upload',
            'last_contacted',
        ]
