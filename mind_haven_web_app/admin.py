from django.contrib import admin

# Register your models here.
from .models import Contacts,Booking, Signup,AdminUser

admin.site.register(Contacts)
admin.site.register(Signup)
admin.site.register(Booking)
admin.site.register(AdminUser)



# Register your models here.
