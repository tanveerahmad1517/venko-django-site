from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget

from .models import Entry


class EntryAdminForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'seo_description': AdminTextareaWidget,
        }
