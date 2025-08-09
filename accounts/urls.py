from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('blogs/', views.blog_list, name='blog_list'),
]
