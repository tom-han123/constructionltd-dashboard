from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect, render
from django.contrib import messages
from .serializers import registerserializer

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from .models import User
from .forms import CreateregisterForm
from django.views.decorators.csrf import csrf_exempt
import json
from .sms import send_otp_to_phone

def dashboard(request):
    return render(request, 'base/index.html')


# Singin & Singup
# @unauthenticated_user
def register(request):
    form = CreateregisterForm()
    if request.method=='POST':
            form = CreateregisterForm(request.POST)
            if form.is_valid():
                user=form.save()
                username = form.cleaned_data.get('name')
                User.objects.create(user=user,name=user.name, phone = user.phone)
                messages.success(request,'Account was created for '+ username)
                return redirect('base:login')
    context={'form':form}
    return render(request,'base/register.html', context)
             
# @unauthenticated_user
def loginpage(request):
    if request.method=='POST':
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            # user=authenticate(request,phone_number=phone,password=password)
            user = User.objects.get(phone_number = phone)
            if user.check_password(password):
                login(request,user)
                return redirect('base:dashboard')
            else:
                messages.info(request,'Email or Password is incorrect! ')
    context={}
    return render(request,'base/login.html')

def forgot(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        otp=request.POST.get('otp')
        return redirect('base:resetpwd')
    context = {}
    return render(request, 'base/forgotpwd.html')

@csrf_exempt
def getotp(request):
    body = request.body.decode('utf-8')
    data = json.loads(body)
    otp = send_otp_to_phone(data['phone'])
    if(otp):
        return JsonResponse({'otp':otp})
    return 'None'

def resetpwd(request):
    context = {}
    return render(request, 'base/resetpwd.html')
                     
def logoutpage(request):
    logout(request)
    return redirect('base:login')








