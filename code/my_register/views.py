from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            print("udalo sie")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect("login_success.html")
    else:
        print("nie udalo sie1")
        form = UserCreationForm()
    print("nie udalo sie2")
    return render(request, "register.html", {"form": form})
