from django import forms
from .models import To_Do_List, To_Do_List_File, DailyLog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class To_Do_ListForm(forms.ModelForm):
    class Meta:
        model = To_Do_List
        fields = [
            'task',
            'task_specifics',
            'files',
            'task_category',
            'task_urgency',
            'task_importance',
            'task_completed',
            'task_followup',
            'task_archive',
        ]

class To_Do_List_FileForm(forms.ModelForm):
    class Meta:
        model = To_Do_List_File
        fields = [
            'uploaded_file',
        ]

class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = [
            'entry_title',
            'entry',
            'good_body_habits',
            'good_mental_habits',
            'good_efficiency_habits',
        ]
