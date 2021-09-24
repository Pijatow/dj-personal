from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index_view(request):
    return render(request, 'account_app/index.html', {})


def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)


def logout_view(request):
    if request.method == 'POST':
        if bool(request.POST.get('logout')):
            logout(request)
            return redirect('index')
    return render(request, 'registration/logout.html', {})
