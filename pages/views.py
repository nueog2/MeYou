from django.shortcuts import render
from mysite.models import Cart


# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def mypage(request):
    return render(request, 'pages/mypage.html')

def login(request):
    return render(request, 'pages/loginpage.html')

