from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('builder/', views.builder, name='builder'),
    path('resume/<str:unique_identifier>/', views.resume, name='resume'),
]