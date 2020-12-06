from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def sayhello(request):
    return HttpResponse("Hello django!")
def hello2(reuest,username):
    return HttpResponse("Hello" + username)
def hello3(request,username):
   now=datetime.now()
   return render(request,"hello3.html",locals())
def hello4(request,username):
   now=datetime.now()
   return render(request,"hello4.html",locals())
