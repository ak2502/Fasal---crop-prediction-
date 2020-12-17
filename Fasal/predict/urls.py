from django.urls import path

from . import views

urlpatterns = [
    path('', views.predict_soil, name='predict'),
    path('result/predict', views.predict_soil, name='predict'),
    path('result/',views.result, name = 'result'),
    path('result/result',views.result, name = 'result'),
    path("login/",views.login, name='login'),
    path("login/login",views.login, name='login'),
    path('register/',views.register, name='register'),
    path("login/register",views.register, name='register'),
    path('register/login',views.login, name='login')
]
