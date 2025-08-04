from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    return render(request, 'login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('home')
