from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('projects')

        else:
            messages.info(request,'invalid username and passwoard')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
