
from django.urls import path

from mind_haven_web_app import views


urlpatterns = [
    path('about', views.about, name="about"),
    path('appointment',views.appointment, name="appointment"),
    path('signup',views.signup, name="signup"),
    
    
    
   
]