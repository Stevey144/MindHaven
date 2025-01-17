from django.contrib import admin

# Register your models here.
from .models import Contacts,Appointment,Booking, Signup

admin.site.register(Contacts)
admin.site.register(Appointment)
admin.site.register(Signup)
admin.site.register(Booking)


# Register your models here.
