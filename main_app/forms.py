# main_app/forms.py

from django import forms
from .models import Maintenance

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'mileage', 'category', 'description']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }