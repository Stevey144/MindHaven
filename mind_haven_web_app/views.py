from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactsForm, SignupForm

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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully signed up!")
            return redirect('home')  
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def about(request):
    return render(request, "mind_haven_web_app/about.html")



def appointment(request):
    return render(request, "mind_haven_web_app/appointment.html")



def signup(request):
    return render(request, "mind_haven_web_app/signup.html")
