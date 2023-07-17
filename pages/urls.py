from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('mainpage/', views.mainpage),
    path('mypage/',views.mypage),
    path('login/',views.login),
    # path('signup/', views.signup),
]