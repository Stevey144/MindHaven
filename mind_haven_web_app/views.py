from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactsForm,SignupForm

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
            form.save()  # Save the user to the database
            messages.success(request, 'Signup successful!')  # Show success message
            return redirect('signup.html')  # Redirect to the desired page (e.g., 'welcome.html')
        else:
            messages.error(request, 'There were some errors in your form. Please check the fields and try again.')  # Show error message
    else:
        form = SignupForm()  # Render an empty form for GET requests

    return render(request, 'mind_haven_web_app/signup.html', {'form': form})


def about(request):
    return render(request, "mind_haven_web_app/about.html")



def appointment(request):
    return render(request, "mind_haven_web_app/appointment.html")
