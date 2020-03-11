from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

def categories(request):
    return render(request, 'blog/categories.html')

def blog(request):
    return render(request, 'blog/blog.html')

def contact(request):
    return render(request, 'blog/contact.html')