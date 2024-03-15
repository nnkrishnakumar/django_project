
from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world")
def home(request):
    return render(request,'hello.html',{"name":"Mohan"})

def add(request):
    val1=request.POST["num1"]
    val2=request.POST["num2"]
    result=eval(val1)+eval(val2)
    return render(request,"result.html",{"result":result})