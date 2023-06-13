from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

from users.models import MyUser as User
# Create your views here.

def home(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.success(request, ("You are already logged in"))
            return redirect('/gallery/')
        return render(request, 'login_signUp.html')
    if request.method == 'POST':
        return render(redirect('login'))




def signUpView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        date_of_birth = request.POST['date_of_birth']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.success(request, ("Email already exists"))
                return redirect('/')
            else:
                user = User.objects.create_user(email=email,date_of_birth= date_of_birth,  password=password)
                user.save()
                login(request, user)
                return redirect('/gallery/')
        else:
            messages.success(request, ("Password does not match"))
            return redirect('/')
    return render(request, 'login_signUp.html')
def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('/gallery/')
        messages.success(request, ("Invalid Credentials"))
        return redirect('/')
    return render(request, 'login_signUp.html')

def logoutView(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('/')