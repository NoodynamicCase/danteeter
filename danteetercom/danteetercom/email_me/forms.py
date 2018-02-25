from django import forms

TOPIC_CHOICES = (
    ('Connect with Dan', 'Connect with Dan'),
    ('Add Content to Website', 'Add Content to Website'),
    ('Other', 'Other'),
    )

class emailForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    comment = forms.CharField(required=True, widget=forms.Textarea)
    email_sender = forms.EmailField(required=True)
