from django.db import models
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
    
    
    def __str__(self):
        return f"{self.FirstName} {self.last} - Phone: {self.phonenumbers}"
    
    
class Appointment(models.Model):
    Email=models.CharField(max_length=100)
    Password= models.CharField(max_length=50)
        
    def __str__(self):
      return self.email


class Signup(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname= models.CharField(max_length=100)
    Email=models.CharField(max_length=100, unique=True)
    Password=models.CharField(max_length=100)
    
    def __str__(self):
      return f"{self.Firstname} {self.Lastname} {self.Email}"
 
class Booking(models.Model):
    date = models.DateField()
    textarea=models.TextField()
    
    def __str__(self):
      return f"{self.date} {self.textarea}"
    
    
    


    
    
    
    
