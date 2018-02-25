from django import forms
from .models import Shopping
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .constants import STORE_CATEGORY_CHOICES
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm

class ShoppingForm(ModelForm):
    class Meta:
        model = Shopping
        # store = forms.ChoiceField(widget=forms.RadioSelect, choices=STORE_CATEGORY_CHOICES)
        fields = (
            'item',
            'specifics',
            'store',
            'item_category',
            'recipient',
            'item_url',
            'picture',
            'wish_list',
            'ordered',
            'favorite',
            'in_list',
            )

        # labels = {
        #     'store' = _('Where to buy?'),
        #     }
        # widgets = {
        #     'store': RadioSelect(),
            # 'name': Textarea(attrs={'cols': 80, 'rows': 20}),
            # }
