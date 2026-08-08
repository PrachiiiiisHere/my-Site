from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout

from django.contrib import messages
from .forms import RegisterForm


# Create your views here.
def register(request):
    form=RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username=form.cleaned_data.get('username')
        messages.success(request,f'Welcome {username}! Your account has been successfully created.')
        return redirect('login')
    
    #for get request
    form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'users/logout.html')