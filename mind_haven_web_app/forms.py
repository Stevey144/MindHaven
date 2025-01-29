from django import forms
from django.forms import EmailInput, ModelForm,DateInput, NumberInput, Select, Textarea,TimeInput,TextInput,IntegerField, ValidationError
from .models import AdminUser, Booking, Contacts,Signup
from django.contrib.auth.hashers import make_password

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
        
        
class SignInForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} is-invalid'
                
                
class AdminSignInForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} is-invalid'
        
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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} is-invalid'
        
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Password and Confirm Password do not match.")
        
        email = cleaned_data.get('email')
        
        if Signup.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance

    
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'textarea']
        widgets = {
            'date': DateInput(attrs={'class': 'form-control', 'id':'mydate'}),
            'textarea': Textarea(attrs={'class': 'form-control', 'cols': 45, 'rows': 10}),
        }
        
class AdminUserForm(ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        label='Confirm Password'
    )  
    class Meta:
        model = AdminUser
        fields = '__all__'  # Include all fields from the Meeting model
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
        
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} is-invalid'
                
           
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Password and Confirm Password do not match.")
        
        email = cleaned_data.get('email')
        
        if AdminUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance
    

