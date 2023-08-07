from .models import Dashboard
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class DashboardForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = ["serial_number", "operator_remarks"]
        widgets = {
            "serial_number": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Enter the serial number'
            }),
            "operator_remarks": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Enter a comment'
            }),
        }

