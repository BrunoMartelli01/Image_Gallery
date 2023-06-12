from django.shortcuts import render

# Create your views here.
def login_signUp(request):
    return render(request, 'login_signUp.html')