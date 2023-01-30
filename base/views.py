from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect, render
from django.contrib import messages
from .serializers import registerserializer
from .models import acc_register


#Admin
def registeration(request, pk=0):
    if request.method == 'POST':
        try:
            if 'register_form' in request.POST:
                phone = request.POST.get('phone')
                password = request.POST.get('pass1')
                repass = request.POST.get('pass2')
                if password == repass:
                    newacc = acc_register.objects.create(phone=phone, password = password)
                    newacc.save()
                    messages.success(request, 'Create new account successful...')
                else: messages.info(request, 'The two passwords does not match each other...')
            elif 'login_form' in request.POST:
                phone = request.POST.get('phone')
                password = request.POST.get('pass')
                acc = acc_register.objects.get(phone=phone)
                if acc.password == password:
                    messages.success(request, 'Login successful...')
                else: messages.info(request, 'Incorrect password...')
        except Exception as e:
            messages.info(request, e)
    return render(request, 'base/login_signup.html')




