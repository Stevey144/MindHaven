from django.shortcuts import render, redirect
from django.contrib import messages

from mind_haven_web_app.models import Signup
from .forms import ContactsForm, SignInForm,SignupForm

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


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']

            try:
                user = Signup.objects.get(email=email, password=password)
                messages.success(request, 'Successfully signed in!')
                return redirect('booking.html')  
            except Signup.DoesNotExist:
                messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = SignInForm()

    return render(request, 'mind_haven_web_app/appointment.html', {'form': form})


def about(request):
    return render(request, "mind_haven_web_app/about.html")

def booking(request):
    return render(request, "mind_haven_web_app/booking.html")

