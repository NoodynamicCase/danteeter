from django import forms
from .models import HumanCapitalPost, HumanCapitalJargon, HumanCapitalSource
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class HumanCapitalPostForm(forms.ModelForm):
    class Meta:
        model = HumanCapitalPost
        fields = [
            'post_topic',
            'post_title',
            'post',
            'sources',
            'upload_file',
            'public_or_private',
            'complete',
        ]

class HumanCapitalJargonForm(forms.ModelForm):
    class Meta:
        model = HumanCapitalJargon
        fields = [
            'word_or_phrase',
            'relates_to',
            'definition',
        ]

class HumanCapitalSourceForm(forms.ModelForm):
    class Meta:
        model = HumanCapitalSource
        fields = [
            'source_title',
            'topic',
            'authors',
            'notes',
            'upload_file_1',
            'upload_file_2',
            'upload_file_3',
            'url_link_1',
            'url_link_2',
            'url_link_3',
        ]
