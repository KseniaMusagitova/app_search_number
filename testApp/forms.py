from .models import Dashboard
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django import forms


class DashboardForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = "__all__"
        widgets = {
            "work_order": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'WORK ORDER'
            }),
            "gap": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'GAP'
            }),
            "data_time": forms.DateTimeInput(attrs={
                "class": 'form-control',
                'placeholder': 'DATA TIME',
                'type': 'datetime-local'
            }),
            "operator_remarks": TextInput(attrs={
                "class": 'form-control',
                'placeholder': "OPERATOR REMARKS"
            }),
        }


class SearchForm(forms.Form):
    work_order = forms.CharField(label='Work order', max_length=20, widget=forms.TextInput(attrs={
        "class": 'form-control',
        'placeholder': 'Search the work order'
    }))