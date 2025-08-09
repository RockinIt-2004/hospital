from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm,BlogForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Blog

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



@login_required
def create_blog(request):
    if request.user.user_type != 'doctor':
        return redirect('home')  # only doctors can create blogs

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('my_blogs')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'my_blogs.html', {'blogs': blogs})

@login_required
def blog_list(request):
    if request.user.user_type != 'patient':
        return redirect('home')

    categories = ['mental_health', 'heart_disease', 'covid19', 'immunization']
    blogs_by_category = {
        cat: Blog.objects.filter(category=cat, draft=False).order_by('-created_at')
        for cat in categories
    }
    return render(request, 'blog_list.html', {'blogs_by_category': blogs_by_category})
