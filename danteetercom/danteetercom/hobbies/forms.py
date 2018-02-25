from django import forms
from .models import Cooking, Guitar
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from tinymce.widgets import TinyMCE

class CookingForm(forms.ModelForm):
    class Meta:
        model = Cooking
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        fields = [
            'title',
            'course',
            'meat',
            'URL_link',
            'ingredients',
            'instructions',
            'tinymce_test',
        ]

class GuitarForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = [
            'artist',
            'song',
            'genre',
            'rating',
            'my_set',
            'tab',
            'url_lyrics',
            'url_link_1',
            'url_link_2',
            'file_1',
            'file_2',
        ]
