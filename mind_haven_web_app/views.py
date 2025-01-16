from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from .forms import ContactsForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact to the database
            messages.success(request, "Contact has been saved successfully.")
            return redirect('welcome.html')  # Redirect to the dashboard or another page
        else:
            messages.error(request, "There was an error saving the contact.")
    else:
        form = ContactsForm()

    return render(request, 'mind_haven_web_app/welcome.html', {'form': form})



def welcome(request):
    return render(request, "mind_haven_web_app/welcome.html")



def about(request):
    return render(request, "mind_haven_web_app/about.html")



def appointment(request):
    return render(request, "mind_haven_web_app/appointment.html")



def signup(request):
    return render(request, "mind_haven_web_app/signup.html")
