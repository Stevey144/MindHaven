
from django.urls import path

from mind_haven_web_app import views


urlpatterns = [
    path('about', views.about, name="about"),
    path('appointment.html',views.sign_in, name="appointment"),
    path('signup.html', views.signup, name='sign-up'),
    path('booking.html', views.booking, name='booking'),
    
]