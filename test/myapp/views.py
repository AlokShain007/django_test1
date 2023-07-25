from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Employee , Owner, Company
from django.urls import reverse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'myapp/home.html')

# use to get data from the front end from form
#employee


def employee(request, id):  # Add the 'id' parameter to the function definition
    if request.method == "POST":
        data = request.POST
        employee_name = data.get('employee_name')
        employee_details = data.get('employee_details')
        owner_id = id
        
        owner = Owner.objects.get(id=owner_id)
        
        Employee.objects.create(
            owner=owner,
            employee_name=employee_name,
            employee_details=employee_details,
        )
        return redirect(reverse('employee', args=[id]))  # Redirect back to the same owner's employee page
    
    else:
        queryset = Employee.objects.filter(owner_id=id)
        request.session['old_id'] = id
        context = {'employee': queryset}
        return render(request, 'myapp/employee.html', context)

# use to delete the data 

def delete_employee(request, id):
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# update employee

def update_employee(request, id):
    queryset = Employee.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        
        employee_name = data.get('employee_name')
        employee_details = data.get('employee_details')
        
        queryset.employee_name = employee_name
        queryset.employee_details =employee_details
        queryset.save()
        old_id=request.session.get('old_id')
        return redirect(f'/employee/{old_id}/')
        
    context ={'employee':queryset}
    
    return render(request, 'myapp/update_employee.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('home')
    
    return render(request, 'myapp/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')
from django.db.models import Q

def register(request):
    
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')
        
        user =User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
         
        user.set_password(password)
        user.save()
        
        messages.info(request, 'Account crated sucessfully')
        return redirect('/register/')
    return render(request,'myapp/register.html')

# for owner

# use to get data from the front end from form

from django.shortcuts import render, redirect, reverse
from .models import Company, Owner

def owner(request, id):
    if request.method == "POST":
        data = request.POST
        owner_name = data.get('owner_name')
        owner_details = data.get('owner_details')
        company_id = id
        company = Company.objects.get(id=company_id)

        # Check if an owner already exists for the company
        if Owner.objects.filter(company_id=company_id).exists():
            return redirect(reverse('owner', args=[id]) + '?error=exists')

        Owner.objects.create(
            company=company,
            owner_name=owner_name,
            owner_details=owner_details,
        )
        return redirect(reverse('owner', args=[id]))
    else:
        queryset = Owner.objects.filter(company_id=id)
        request.session['old_id'] = id
        context = {'owner': queryset}

    return render(request, 'myapp/owner.html', context)

def delete_owner(request, id):
    queryset = Owner.objects.get(id = id)
    queryset.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_owner(request, id):
    queryset = Owner.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        
        owner_name = data.get('owner_name')
        owner_details = data.get('owner_details')
        
        queryset.owner_name = owner_name
        queryset.owner_details =owner_details
        queryset.save()
        old_id=request.session.get('old_id')
        return redirect(f'/owner/{old_id}/')

    context ={'owner':queryset}
    
    return render(request, 'myapp/update_owner.html', context)


#company 

#@login_required(login_url="/login/")
def company(request):
    if request.method == "POST":
        data = request.POST
        company_name = data.get('company_name')
        company_details = data.get('company_details')
        
        Company.objects.create(
            company_name=company_name,
            company_details=company_details,
        )
        return redirect('/company/')

    queryset = Company.objects.all()
    context = {'company': queryset}
    return render(request, 'myapp/company.html', context)

def delete_company(request, id):
    queryset = Company.objects.get(id=id)
    queryset.delete()
    return redirect('/company/')

def update_company(request, id):
    queryset = Company.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        company_name = data.get('company_name')
        company_details = data.get('company_details')

        queryset.company_name = company_name
        queryset.company_details = company_details
        queryset.save()
        return redirect('/company/')

    context = {'company': queryset}
    return render(request, 'myapp/update_company.html', context)

#intern

def intern(request, id):
    if request.method == "POST":
        data = request.POST
        intern_name = data.get('intern_name')
        intern_details = data.get('intern_details')
        employee_id = id  # Assuming you are passing employee_id as a hidden field in the form

        # Get the corresponding employee for the intern
        employee = Employee.objects.get(id=employee_id)

        # Create a new Intern object associated with the employee
        Intern.objects.create(
            employee=employee,
            intern_name=intern_name,
            intern_details=intern_details,
        )
        return redirect(reverse('intern', args=[id]))# Redirect to the intern page after adding an intern

    else:
        # This block will handle the GET request to view the intern data

        # Get the queryset of interns associated with the employee (id)
        queryset = Intern.objects.filter(employee_id=id)
        request.session['old_id']=id
        
        # Pass the queryset to the template for rendering
        context = {'intern': queryset}

        return render(request, 'myapp/intern.html', context)



def delete_intern(request, id):
    queryset = Intern.objects.get(id=id)
    queryset.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_intern(request, id):
    queryset = Intern.objects.get(id=id)

    if request.method == "POST":
        data = request.POST        
        intern_name = data.get('intern_name')        
        intern_details = data.get('intern_details')        
        queryset.intern_name = intern_name
        queryset.intern_details = intern_details
        queryset.save()
        old_id=request.session.get('old_id')
        return redirect(f'/intern/{old_id}/')

    context = {'intern': queryset}
    return render(request, 'myapp/update_intern.html', context)

