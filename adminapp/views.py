from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# Create your views here.
from django.shortcuts import render

def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method == "POST":
        User_input=request.POST['User_input']
        print(f'User input:{User_input}')
    a1={'User_input':User_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method == 'POST':
        user_input=request.POST['user_input']
        result=None
        error_message=None
        try:
            num=int(user_input)
            result=10/num
        except Exception as e:
            error_message=str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})
    return render(request,'adminapp/ExceptionExample.html')



def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/ProjectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks} )


def delete_task(request , pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/Register.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        email = request.POST['Email']
        pass1 = request.POST['Password']
        pass2 = request.POST['ConformPassword']

        if pass1 == pass2:
            if User.objects.filter(Username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(Email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    Username=username,
                    Password=pass1,
                    Firstname=first_name,
                    Lastname=last_name,
                    Email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegister.html')

from django.contrib import messages
from django.contrib.auth import authenticate,login

def UserLoginPageCall(request):
    return render(request,'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        password=request.POST.get('Password')
        print(username)
        user=authenticate(request, Username=username, Password=password)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')
            elif len(username)==4:
                return redirect('facultyapp:FacultyHomePage')
            else:
                messages.error(request,'Username length does not match student or faculty criteria.')
                return render(request,'adminapp/Login.html')

    return render(request, 'adminapp/Login.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from .forms import StudentForm
from .models import StudentList
#def add_student(request):
 #   if request.method =='POST':
  #      form = StudentForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('student_list')
   # else:
    #    form = StudentForm()
   # return render(request, 'adminapp/add_student.html', {'form':form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html',{'students': students})


def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')
import datetime
import calendar
from datetime import timedelta

from datetime import datetime, timedelta
import calendar
from django.shortcuts import render
def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST['date1'])
        x = datetime.now()
        ran = x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not a Leap Year"
        else:
            ran3 = "Leap Year"
        a1 = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    else:
        a1 = {'ran': None, 'ran3': None, 'ran1': None, 'number1': None}

    return render(request, 'adminapp/datetimepage.html', a1)

import random
import string

def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran':ran}
    return render(request,'adminapp/randomexample.html',a1)

def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')
def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})