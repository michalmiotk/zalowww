from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_gui(request):
    return render(request, "login.html")

def login_machine(request):
    print("witam na login machine")
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    if request.user.is_authenticated:
        return redirect('home')
    else:
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("zalogowano")
            return render(request, "login_success.html")
        else:
            print("problem z logowaniem")
            return render(request, "login_bad.html")