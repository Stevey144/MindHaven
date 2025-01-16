from django import forms
from django.forms import ModelForm,DateInput, NumberInput, Select,TimeInput,TextInput,IntegerField
from django.core.exceptions import ValidationError

from .models import Contacts
from .models import Signup

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'gender': forms.Select(choices=Contacts.GENDER_CHOICES),
            'disability': forms.Select(choices=Contacts.DISABILITY_CHOICES),
        }
        
class SignupForm(forms.ModelForm):
    # Adding password validation to ensure the password is entered twice for confirmation
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    class Meta:
        model = Signup
        fields = ['Firstname', 'Lastname', 'Email', 'Password']
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('Password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password

