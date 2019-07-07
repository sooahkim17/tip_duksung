from django.shortcuts import render, redirect
from .models import Login
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from tip import templates,views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,HttpResponse

####################################################
# Create your views here.


def login(request):

    if request.method == 'POST':

            username = request.POST.get('username')

            password = request.POST.get('password')

            user = auth.authenticate(request, username=username, password=password)

            if user :
        
                auth_login(request, user)

                return render(request,'login_show.html')

            else:

                return render(request, 'login_show.html', {'error': 'username or password is incorrect.'})

    else:
        form=LoginForm()

        return render(request, 'login.html',{'form':form})


@login_required
def logout(request):

    if request.method == 'POST':

        auth_logout(request)

        return render(request,'login_show.html')

    return redirect('logout')

