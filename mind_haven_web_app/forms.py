from django import forms
from django.forms import ModelForm,DateInput, NumberInput, Select,TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError

from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'gender': forms.Select(choices=Contacts.GENDER_CHOICES),
            'disability': forms.Select(choices=Contacts.DISABILITY_CHOICES),
        }

