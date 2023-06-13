from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from images.models import Image
from users.utils import get_tokens_for_user

def gallery(request):

    if request.user.is_authenticated:
        images = Image.objects.filter(user=request.user)
        nameImg = []
        for img in images:
            name = img.image.name.replace('media/', '')
            nameImg.append(name)
        context = {'images': nameImg}
        return render(request, 'gallery.html', context)
    else:
        messages.success(request, ("Please login first"))
        return redirect('/')

def getToken(request):
    if request.user.is_authenticated:
        messages.success(request,get_tokens_for_user(request.user)['access'])
        return redirect('/gallery/')
    else:
        messages.success(request, ("Please login first"))
        return redirect('/')