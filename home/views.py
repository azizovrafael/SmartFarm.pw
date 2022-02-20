from django.shortcuts import render
from .models import *

def home_view(request):
    contact = Contact.objects.all()
    contact_us = Contact_Us.objects.all()
    contact_us_punk = Contact_Us_Punk.objects.all()
    services = Services.objects.all()
    project = Project.objects.all()
    return render(request, "index.html", {"contact":contact,
                                          "contact_us":contact_us,
                                          "contact_us_punk":contact_us_punk,
                                          "services":services,
                                          "project":project,
                                          })
