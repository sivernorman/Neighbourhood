from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm,PostForm
from .models import Profile,Neighbourhood,Post,HoodDetails

 


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    details=HoodDetails.objects.all()
    posts=Post.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        postform = PostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        if postform.is_valid():
            post = postform.save(commit=False)
            post.user = current_user
            post.neighbourhood = current_user.profile.neighbourhood
            post.save()
    else:
        form = ProfileForm()
        postform = PostForm()
    return render(request, 'profile.html',{"form":form,"posts":posts,"postform":postform,"details":details})

def timeline(request):
    hoods=Neighbourhood.objects.all()
    return render(request, 'timeline.html',{"hoods":hoods})
