from django.shortcuts import render, get_object_or_404
from .models import CabUser, CabDriver
# Create your views here.

def callLogInPage(request):
    return render(request, 'find_your_cab/login.html', '')

def callHomePage(request):
    driv_inform = CabDriver.objects.order_by('-point')
    user_inform = CabUser.objects.order_by('password_user')
    try:
        name = request.POST['name']
        password = request.POST['password']
    except:
        name = ''
        password = 0
    for cabuser in user_inform :
        if name == cabuser.name_user :
            if int(password) == cabuser.password_user :
                user_inform = get_object_or_404(CabUser, pk=cabuser.id)
                return render(request, 'find_your_cab/home.html', {'driv_inform':driv_inform, 'user_inform':user_inform})
    return render(request, 'find_your_cab/login.html', '')

def callRatePage(request, cab_id):
    driv_inform = get_object_or_404(CabDriver, pk=cab_id)
    return render(request, 'find_your_cab/rate_page.html', {'driv_inform':driv_inform})

def savePoint(request, cab_id):
    driv_inform = CabDriver.objects.order_by('-point')
    cab_driv = get_object_or_404(CabDriver, pk=cab_id)
    try:
        point = request.POST['point']
    except:
        point = 0
    before_point = cab_driv.point
    cab_driv.point = (before_point + int(point))/2
    cab_driv.save()
    return render(request, 'find_your_cab/thank_page.html', '')

  


