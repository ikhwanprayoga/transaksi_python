from django.shortcuts import render, redirect
from django.http import HttpResponse
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/index')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "post.html", {'form':form})
        
def index(request):
    employees = Employee.objects.all()
    return render(request, "index.html", {'employees':employees})

def show(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "show.html", {'employee':employee})
        
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid:
      form.save()
      return redirect('/index')
    return render(request, "edit.html", {'employees':employees})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/index')

def tes(request):
    data = Employee.objects.all()
    return HttpResponse(data)