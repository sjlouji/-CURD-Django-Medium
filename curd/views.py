from django.shortcuts import render, redirect
from .models import Emp
from django.contrib import messages

# Create your views here.

def createView(request):
    return render(request,'create.html')


def store(request):
    emp = Emp()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Added Successfully")
    return redirect('/create')



def index(request):
    emp = Emp.objects.all()
    return render(request, 'index.html',{'emp':emp})
    
def updateView(request,pk):
    emp = Emp.objects.get(id = pk)
    return render(request,'update.html',{'emp':emp})



def update(request,pk):
    print('in')
    emp = Emp.objects.get(id = pk)
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Update Successfully")
    return redirect('/')

def deleteEmp(request, pk):
    emp = Emp.objects.get(id = pk)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('/')


def viewEmp(request,pk):
    emp = Emp.objects.get(id = pk)
    return render(request, 'view.html',{'emp':emp})