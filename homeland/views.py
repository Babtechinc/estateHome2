from django.shortcuts import render,redirect
from django.contrib import messages,auth
from listing.models import listi_ng
from django.http import HttpResponse
from django.contrib.auth.models import User
from agent.models import agent

from homeland.option import price,sq_ft,baths,beds,property_type,location
# Create your views here.
def index(respond):
    listin = listi_ng.objects.order_by('price')[:6]
    agentlist = agent.objects.order_by('name')[:4]
    listin_dict =  {'key':listin,'agentdict': agentlist,'price': price,
            'sq_ft': sq_ft,
            'baths': baths,
            'beds': beds,
            'location':location,
            'property_type':property_type}
    return render(respond, 'index.html',context=listin_dict)
def contact(respond):
    contact_dict = { 'price': price,
                   'sq_ft': sq_ft,
                   'baths': baths,
                   'beds': beds,
                   'location': location,
                   'property_type': property_type}
    return render(respond, 'contact.html', context=contact_dict)
def try1(respond):
    return HttpResponse('heyyy')
def search(respond):
    listin = listi_ng.objects.order_by('street')

    if 'bed' in respond.GET:
        bed= respond.GET['bed']
        if bed:
            listin = listin.filter(bedrooms__exact=bed)
    if 'bath' in respond.GET :
        bath = respond.GET['bath']
        if bath:
            listin = listin.filter(bathroom__exact=bath)
    if 'deal' in respond.GET:
        deal1 = respond.GET['deal']
        if deal1 != 'any':
            listin = listin.filter(deal__contains=deal1)
    if 'property' in respond.GET:
        property = respond.GET['property']
        if property != 'any':
            listin = listin.filter(type_listing__contains=property)
    if 'sqft' in respond.GET:
        sqft = respond.GET['sqft']
        if sqft != 'any':
            listin = listin.filter(SqFt__gt=sqft)
    if 'min_price' in respond.GET:
        min_price = respond.GET['min_price']
        if min_price != 'any':
            listin = listin.filter(price__gt=min_price)
    if 'max_price' in respond.GET:
        max_price = respond.GET['max_price']
        if max_price != 'any':
            listin = listin.filter(price__lt=max_price)
    if 'location' in respond.GET:
        location2 = respond.GET['location']
        if location2 != 'any':
            listin = listin.filter(location__contains=location2)
    listin_dict = {'key': listin,  'price': price,
                   'sq_ft': sq_ft,
                   'baths': baths,
                   'beds': beds,
                   'location': location,
                   'property_type': property_type,
                   'values':respond.GET, }
    return render(respond,'search.html',context=listin_dict)

def loginPage(respond):
    if respond.method =='POST':
        username1 = respond.POST["username1"]
        password = respond.POST["password"]
        user= auth.authenticate(username=username1,password=password)
        if user is not None:
            auth.login(respond,user)
            messages.success(respond,'welcome')
            return redirect('index')
        else:
            messages.error(respond,'YOUR INFORMATION IS WORNG')
    return render(respond,'login.html',context={})

def registerPage(respond):
    if respond.method =='POST':
        full_name = respond.POST['fullname']
        user_name = respond.POST['username']
        email = respond.POST['email']
        password = respond.POST['password']
        password1 = respond.POST['password2']
        if password == password1:
            if User.objects.filter(username=user_name).exists():
                messages.error(respond, 'username exist')
                redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(respond, 'email exist')
                    redirect('register')
                else:
                    user =User.objects.create_user(username=user_name,email=email,password=password,first_name=full_name)
                    user.save()
                    messages.success(respond, 'you are register')
                    redirect('login')
        else:
            messages.error(respond,'check your pass and try again')
            redirect('register')
    return render(respond,'register.html',context={})