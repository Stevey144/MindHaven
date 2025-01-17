"""
URL configuration for mindhaven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mind_haven_web_app import views
from mind_haven_web_app.views import contact_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html',contact_view, name="welcome"),
    path('',contact_view),
    path('signup',views.signup, name="signup"),
    path('mindhaven/', include('mind_haven_web_app.urls'))
]
