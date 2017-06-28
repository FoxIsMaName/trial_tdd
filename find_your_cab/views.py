from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import CabUser, CabDriver, DriverHistory
import math
# Create your views here.

#call page that user can use to input their username and password
def callLogInPage(request):
    return render(request, 'find_your_cab/login.html', '')

#call home page by use password
def callHomePage(request):
    #call objects from User class
    user_inform = User.objects.all()

    #get name and password from login page
    name = request.POST['name']
    password = request.POST['password']

    #authenticate username and password 
    user = authenticate(username=name, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return render(request, 'find_your_cab/home.html', {'user':user})
    else:
        # No backend authenticated the credentials
        return render(request, 'find_your_cab/login.html', '')

#use to rate each driver
def callRatePage(request, user_id):     
    #call objects from CabDriver and User
    driv_inform = CabDriver.objects.order_by('-point')
    user_inform = User.objects.get(id=user_id)

    #get driver name from home page
    try:
        name_driv = request.POST['name_driv']
    except:
        name = ''

    #check "Does driver that user inputed is in the cabdriver class?"
    for cabdriver in driv_inform :
        if name_driv == cabdriver.name_driver :
            #get objectt from CabDriver class
            driv_inform = get_object_or_404(CabDriver, pk=cabdriver.id)
    return render(request, 'find_your_cab/rate_page.html', {'driv_inform':driv_inform, 'user_inform':user_inform})

#save point from rate input by user
def savePoint(request, cab_id, user_id):
    #call objects from CabDriver and User
    driv_inform = get_object_or_404(CabDriver, pk=cab_id)
    user_inform = User.objects.get(id=user_id)

    #check if point and comment are input are inputed
    try:
        point = request.POST['point']
        comment = request.POST['comment']
    except:
        point = 0
        comment = ''
    
    #save point and comment to driverhistory class
    driv_inform.driverhistory_set.create(cab_user=user_inform.username, driv_point = point, comment = comment)

    #call history driver to 
    history_driv = DriverHistory.objects.order_by('driv_point') 
    n = 0
    point_sum = 0   
    for driverhistory in history_driv :
        print( driverhistory.driv_point)
        #if history_driv.cab_driver == driv_inform.name_driver :
        n = n + 1
        point_sum = point_sum + driverhistory.driv_point
    #log out this user
    logout(request)
    #average point
    driv_inform.point = math.ceil(point_sum/n)
    #save point to data base
    driv_inform.save()
    return render(request, 'find_your_cab/thank_page.html', '')

#let user sign in if they don't have an account 
def callSignInPage(request):
    return render(request, 'find_your_cab/signin.html', '')

#save user data
def saveUser(request):
    try:
        name = request.POST['name']
        password = request.POST['password']
    except:
        name = ''
        password = 0
    #save user information to data base
    cabuser = User.objects.create_user(username=name, password=password)
    cabuser.save()
    return render(request, 'find_your_cab/show_inform.html', {'name':name})

#call page that tell what is this app have
def callAboutPage(request):
    return render(request, 'find_your_cab/aboutpage.html', '')
