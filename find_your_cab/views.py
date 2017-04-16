from django.shortcuts import render, get_object_or_404
from .models import CabUser, CabDriver
# Create your views here.

def callHomePage(request):
    driv_inform = CabDriver.objects.order_by('-point')
    return render(request, 'find_your_cab/home.html', {'driv_inform':driv_inform})

def callRatePage(request, cab_id):
    driv_inform = get_object_or_404(CabDriver, pk=cab_id)
    return render(request, 'find_your_cab/rate_page.html', {'driv_inform':driv_inform})


