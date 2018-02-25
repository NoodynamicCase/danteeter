from django import forms
from .models import Blog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'post_title',
            'post_category',
            'post_entry',
            'public_private',
        ]
