from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm


import sweetify

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/1')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                sweetify.success(request, 'با موفقیت وارد شدید!', text='شما می‌توانید تست را انجام بدهید', type='success', timer=2000)
                login(request, user)
                return redirect('/1')
            else:
                sweetify.error(request, 'Oops...', text='wrong username or email entered. - reload the site', persistent='close', type='error')
        else:
            sweetify.error(request, 'Oops...', text='Invalid form submission.', persistent='close', type='error')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                sweetify.success(request,'ثبت‌نام با موفقیت انجام شد',text='شما می‌توانید تست را انجام بدهید.', type='success',timer=2000)
                return redirect('/1')

        form = UserCreationForm()
        context = {'form':form}
        return render(request,'accounts/pages-register.html',context)
    else:
        return redirect('/')

