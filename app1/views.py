from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'index.html')

# About page view
def downloads(request):
    return render(request, 'downloads.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

