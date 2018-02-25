from django import forms
from .models import Timer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = [
            'task_category',
            'task_description',
        ]
