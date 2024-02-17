from django.shortcuts import render

# Home page
def index(request):
    return render(request, 'index.html', {})

# About page
def about(request):
    return render(request, 'about.html', {})

# Contact page
def contact(request):
    return render(request, 'contact.html', {})
