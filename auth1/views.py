from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm

def loginUserView(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('registerUser')
    
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('registerUser')

    else:
        form = LoginForm()
    
    context['login_form'] = form
    return render(request, 'auth1/login.html', context)

def registerUserView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'auth1/register.html', context)


def logoutUserView(request):
    logout(request)
    return redirect('home')




