from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
import logging
from users.models import MyUser as User
# Create your views here.

def home(request):
    logger = logging.getLogger(__name__)
    if request.method == 'GET':
        return render(request, 'login_signUp.html')
    if request.method == 'POST':
        logger.warning("Platform is running at risk")
        return render(redirect('login'))




def signUpView(request):
    logger = logging.getLogger(__name__)
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        date_of_birth = request.POST['date_of_birth']
        logger.warning(email)
        logger.warning(password)
        logger.warning(password2)
        logger.warning(date_of_birth)
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.success(request, ("Email already exists"))
                return redirect('/')
            else:
                user = User.objects.create_user(email=email,date_of_birth= date_of_birth,  password=password)
                user.save()

                messages.success(request, ("Registration Successful"))
                return redirect('/')
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

            return render(request, 'yep.html')
        messages.success(request, ("Invalid Credentials"))
        return redirect('/')
    return render(request, 'login_signUp.html')

