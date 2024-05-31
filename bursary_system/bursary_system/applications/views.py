from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BursaryApplicationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import BursaryApplication 
from .models import Allocation
from .forms import InstitutionForm



@login_required
def apply_bursary(request):
    if request.method == 'POST':
        form = BursaryApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application_success')
    else:
        form = BursaryApplicationForm()
    return render(request, 'applications/apply_bursary.html', {'form': form})

def application_success(request):
    return render(request, 'applications/application_success.html')
def home(request):
    return render(request, 'applications/home.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
def check_allocation(request, student_type):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            institution = form.cleaned_data['institution']

            if student_type == 'highschool':
                allocation_amount = 10000
            elif student_type == 'college':
                allocation_amount = 10000
            elif student_type == 'university':
                allocation_amount = 10000
            else:
                return HttpResponse('Invalid student type')

            context = {
                'institution': institution,
                'allocation_amount': allocation_amount
            }
            return render(request, 'check_allocation.html', context)
        else:
            # Handle form not valid case
            return render(request, 'institution_form.html', {'form': form})
    else:
        form = InstitutionForm()
        return render(request, 'institution_form.html', {'form': form})