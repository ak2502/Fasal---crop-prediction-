from django.shortcuts import render, redirect
from predict.models import soil
import pandas as pd 
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


def predict_soil(request):
    Soil = soil.objects.all()
    context = {
        'predict':Soil
    }
    return render(request, 'index.html',context)


def predictions(soil):
   
    df = pd.read_csv('predict/dataset.csv')
    df_new=df[df.soil==soil]
    df_new.sort_values('average_cost',axis=0,ascending=True,inplace=True)
    crop=[]
    cost=[]
    crop.append(df_new['crop'].head(2))
    cost.append(df_new['average_cost'].head(2))
    return crop,cost

def result(request):
    soil = (request.GET['soil'])
    print(soil)
    crop,cost = predictions(soil)
    result=zip(crop,cost)
    return render(request, 'result.html', {'result':result})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        username= request.POST['username']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,"username taken!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("email alredy taken")
                messages.info(request,"email already taken!")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                messages.info(request,"user created")
                return redirect('login')
        else:
            print("wrong password")
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def login(request):
    
    if request.method == 'POST':
        password = request.POST['password']
        username= request.POST['username']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials!")    
            return redirect('login')


    else:    
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
