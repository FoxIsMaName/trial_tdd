from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import CabUser, CabDriver, DriverHistory
import math
# Create your views here.

def callLogInPage(request):
    return render(request, 'find_your_cab/login.html', '')

def callHomePage(request):

    user_inform = User.objects.all()
    name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username=name, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return render(request, 'find_your_cab/home.html', {'user':user})
    else:
        # No backend authenticated the credentials
        return render(request, 'find_your_cab/login.html', '')

def callRatePage(request, user_id):    
    driv_inform = CabDriver.objects.order_by('-point')
    user_inform = User.objects.get(id=user_id)
    try:
        name_driv = request.POST['name_driv']
    except:
        name = ''
    for cabdriver in driv_inform :
        if name_driv == cabdriver.name_driver :
            driv_inform = get_object_or_404(CabDriver, pk=cabdriver.id)
    return render(request, 'find_your_cab/rate_page.html', {'driv_inform':driv_inform, 'user_inform':user_inform})

def savePoint(request, cab_id, user_id):
    driv_inform = get_object_or_404(CabDriver, pk=cab_id)
    user_inform = User.objects.get(id=user_id)
    try:
        point = request.POST['point']
    except:
        point = 0
    driv_inform.driverhistory_set.create(cab_user=user_inform.username, driv_point = point)

    history_driv = DriverHistory.objects.order_by('driv_point') 
    n = 0
    point_sum = 0   
    for driverhistory in history_driv :
        n = n + 1
        point_sum = point_sum + driverhistory.driv_point
    logout(request)
    driv_inform.point = math.ceil(point_sum/n)
    driv_inform.save()
    return render(request, 'find_your_cab/thank_page.html', '')

def callSignInPage(request):
    return render(request, 'find_your_cab/signin.html', '')

def saveUser(request):
    try:
        name = request.POST['name']
        password = request.POST['password']
    except:
        name = ''
        password = 0
    cabuser = User.objects.create_user(username=name, password=password)
    cabuser.save()
    return render(request, 'find_your_cab/show_inform.html', {'name':name})


