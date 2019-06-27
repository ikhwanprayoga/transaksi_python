from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # employees = Employee.objects.all()
    return render(request, "users/index.html")