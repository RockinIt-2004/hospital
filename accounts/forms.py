from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Blog

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'profile_pic', 'username',
            'email', 'password1', 'password2',
            'address_line1', 'city', 'state', 'pincode', 'user_type'
        ]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
