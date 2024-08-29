from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.type_staff == 'admin':
                    return redirect('admin_home')
                elif user.type_staff == 'seller':
                    return redirect('seller_home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def admin_home(request):
    return render(request, 'admin.html')


@login_required
def seller_home(request):
    return render(request, 'seller.html')


def logout_page(request):
    logout(request)
    return redirect('home')
