from django import forms
from django.forms import EmailInput, ModelForm,DateInput, NumberInput, Select,TimeInput,TextInput,IntegerField, ValidationError
from .models import Contacts,Signup

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['FirstName', 'last', 'phonenumbers', 'address','gender','disability']
        widgets = {
            'FirstName': TextInput(attrs={'class': 'form-control'}),
            'last': TextInput(attrs={'class': 'form-control'}),
            'phonenumbers': NumberInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=Contacts.GENDER_CHOICES),
            'disability': forms.Select(choices=Contacts.DISABILITY_CHOICES),
        }
        
class SignupForm(ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        label='Confirm Password'
    )
     
    class Meta:
        model = Signup
        fields = '__all__'  # Include all fields from the Meeting model
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        # Check if password and confirm password match
        if password != confirm_password:
            raise ValidationError("Password and Confirm Password do not match.")
        
        # Check if email or username already exists
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        
        if Signup.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        
        if Signup.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        
        return cleaned_data

