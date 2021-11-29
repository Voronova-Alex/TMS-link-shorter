from django import forms
from django.forms import ModelForm
from .models import Link



class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['input_link',]
        widgets = {
            'input_link':forms.TextInput(attrs={'placeholder': 'Введите ссылку для сокращения'}),
        }