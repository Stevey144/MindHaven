from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, "mind_haven_web_app/welcome.html")

def about(request):
    return render(request, "mind_haven_web_app/about.html")

def appointment(request):
    return render(request, "mind_haven_web_app/appointment.html")

def signup(request):
    return render(request, "mind_haven_web_app/signup.html")
