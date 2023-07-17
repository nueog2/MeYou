from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def mypage(request):
    return render(request, 'pages/mypage.html')

def login(request):
    return render(request, 'accounts/login.html')

