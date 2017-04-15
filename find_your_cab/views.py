from django.shortcuts import render

# Create your views here.

def callHomePage(request):
    return render(request, 'find_your_cab/home.html', '')
