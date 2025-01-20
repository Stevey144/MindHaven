from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from mind_haven_web_app.models import AdminUser, Booking, Signup
from .forms import AdminSignInForm, AdminUserForm, BookingForm, ContactsForm, SignInForm,SignupForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact has been saved successfully.")
            return redirect('welcome.html')
        else:
            messages.error(request, "There was an error saving the contact.")
    else:
        form = ContactsForm()

    return render(request, 'mind_haven_web_app/welcome.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Signup successful!') 
            return redirect('signup.html') 
        else:
            messages.error(request, 'There were some errors in your form. Please check the fields and try again.')  # Show error message
    else:
        form = SignupForm()  

    return render(request, 'mind_haven_web_app/signup.html', {'form': form})

def admin_sign_up_view(request):
     if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Admin User Created! please Sign In') 
        else:
            messages.error(request, 'There were some errors in your form. Please check the fields and try again.')  # Show error message
     else:
        form = AdminUserForm()  

     return render(request, 'mind_haven_web_app/admin-sign-up.html', {'form': form})
 
 
def admin_sign_in_view(request):
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            try:
                admin_user = AdminUser.objects.get(email=email)

                if check_password(password, admin_user.password):
                    request.session['admin_user_email'] = admin_user.email
                    messages.success(request, 'Admin Login Successful!')
                else:
                    messages.error(request, 'Invalid email or password. Please try again.')
            except AdminUser.DoesNotExist:
                messages.error(request, 'Invalid email or password. Please try again.')

    else:
        form = AdminSignInForm()

    return render(request, 'mind_haven_web_app/admin-sign-in.html', {'form': form})


def sign_in(request): 
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            try:
                user = Signup.objects.get(email=email)
                if check_password(password, user.password):
                    request.session['user_email'] = user.email 
                    messages.success(request, 'Successfully signed in!')
                else:
                    messages.error(request, 'Invalid email or password. Please try again.')
            except Signup.DoesNotExist:
                messages.error(request, 'Invalid email or password. Please try again.')

    else:
        form = SignInForm()

    return render(request, 'mind_haven_web_app/appointment.html', {'form': form})

def booking(request):
    
    if 'user_email' not in request.session:
        return redirect('appointment')
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_fields = form.save()
            booking_date =  booking_fields.date
            messages.success(request,  f'Appointment Booked for {booking_date}. Please plan to attend.')
        else:
            messages.error(request, 'There was an error in booking this Appointment, please try again')
    else:
        form = BookingForm()  

    return render(request, 'mind_haven_web_app/booking.html', {'form': form})

def booking_list(request):
    if 'admin_user_email' not in request.session:
        return redirect('admin-sign-in')
    return render(request, "mind_haven_web_app/view-booking.html", {"booking_list" : Booking.objects.all()})
