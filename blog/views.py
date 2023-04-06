from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from blog.forms import PhotoForm

from . import forms, models


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})


@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos})


@login_required
def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm()
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/Profile.html', context={'form': form})

