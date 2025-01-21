
from django.urls import path

from mind_haven_web_app import views

urlpatterns = [
    path('appointment.html',views.sign_in, name="appointment"),
    path('signup.html', views.signup, name='sign-up'),
    path('booking.html', views.booking, name='booking'),
    path('admin/admin-sign-up.html', views.admin_sign_up_view, name='admin-sign-up'), 
    path('admin/admin-sign-in.html', views.admin_sign_in_view, name='admin-sign-in'), 
    path('admin/view-booking.html', views.booking_list, name='view-booking'), 
    path('admin/view-booking-details.html/<int:id>/', views.booking_detail, name="booking_detail"),
    path('admin/booking.html/<int:id>/', views.edit_booking_details, name='edit_booking_detail'), 
    path('admin/delete-Booking/<int:id>/', views.delete_booking, name="delete_booking"),
]