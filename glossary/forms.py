from django import forms

from .models import Acronym


class AcronymForm(forms.ModelForm):
    class Meta:
        model = Acronym
        fields = ('abbreviation', 'word',)
