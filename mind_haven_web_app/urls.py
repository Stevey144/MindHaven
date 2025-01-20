
from django.urls import path

from mind_haven_web_app import views

urlpatterns = [
    path('appointment.html',views.sign_in, name="appointment"),
    path('signup.html', views.signup, name='sign-up'),
    path('booking.html', views.booking, name='booking'),
    path('admin-sign-up.html', views.admin_sign_up_view, name='admin-sign-up'), 
    path('admin-sign-in.html', views.admin_sign_in_view, name='admin-sign-in'), 
    path('view-booking.html', views.booking_list, name='view-booking'),  
]