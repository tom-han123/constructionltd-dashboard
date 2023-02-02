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
from datetime import datetime

def dashboard(request):
    return render(request, 'base/index.html')


expire = 120

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
        user = User.objects.get(phone_number=phone)
        if user:
            if otp == user.otp:
                t1 = user.set_otp_time
                t2 = datetime.now().astimezone()
                t = t2 - t1
                if t.total_seconds() < expire:
                    return redirect('base:resetpwd', pk=user.id)
                    # context = {'phone':phone}
                    # return render(request, 'base/resetpwd.html', context)
                else:
                    messages.info(request, "Your verification code is expire, please request otp again.")
            else: messages.info(request, "Incorrect verification code.")
        else: messages.info(request, "Incorrect phone number.")
    
    return render(request, 'base/forgotpwd.html')

@csrf_exempt
def getotp(request):
    try:
        body = request.body.decode('utf-8')
        data = json.loads(body)
        user = User.objects.get(phone_number=data['phone'])
        otp = send_otp_to_phone(data['phone'])
        user.otp = otp
        user.set_otp_time = datetime.now()
        user.save()
        if(otp):
            return JsonResponse({'otp':otp})
    except Exception as e:
        return JsonResponse({'otp':'None'})

def resetpwd(request, pk):
    if request.method == 'POST':
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user = User.objects.get(id=int(pk))
            return redirect('base:dashboard')
        messages.info(request,'The two password does not match each other.')
    return render(request, 'base/resetpwd.html')
                     
def logoutpage(request):
    logout(request)
    return redirect('base:login')








