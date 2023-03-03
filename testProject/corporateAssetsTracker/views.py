from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Company

def add_company(request):
    company = Company.objects.all()
    return render(request, "add_company.html");
