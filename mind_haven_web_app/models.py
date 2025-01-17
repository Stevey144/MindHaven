from datetime import time
from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Contacts(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    DISABILITY_CHOICES = [
        ('yes', 'Yes, I have a disability, or have had one in the past'),
        ('no', 'No, I do not have a disability and have not had one in the past'),
        ('no_answer', 'I do not want to answer'),
    ]
    
    FirstName=models.CharField(max_length=50)
    last=models.CharField(max_length=50)
    phonenumbers=models.IntegerField()
    address=models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    disability = models.CharField(max_length=15, choices=DISABILITY_CHOICES, default='no')
    
    
    def __str__(self):
        return f"{self.FirstName} {self.last} - Phone: {self.phonenumbers}"
    
    
class Appointment(models.Model):
    Email=models.CharField(max_length=100)
    Password= models.CharField(max_length=50)
        
    def __str__(self):
      return self.email


class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=255)
    
    def __str__(self):
       return f"{self.first_name} {self.last_name} {self.email}"
 
class Booking(models.Model):
    date = models.DateField()
    textarea=models.TextField()
    
    def __str__(self):
      return f"{self.date} {self.textarea}"
    
    
    


    
    
    
    
