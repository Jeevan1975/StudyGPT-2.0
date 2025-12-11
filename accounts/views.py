from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm, RegisterForm




def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
        
    return render(request, 'accounts/signup.html', context)




def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('dashboard:dashboard')
            else:
                form.add_error(None, "Invalid email or password. Please try again.")
                
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    
    return render(request, 'accounts/login.html', context)