from django.shortcuts import render

# Create your views here.
# blog/views.py
def home(request):
    return render(request, 'blog/home.html')