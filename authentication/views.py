
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from authentication.models import User
from .models import Comics





from . import forms
from blog.models import Comics


# def home(request):

#     paginator = Paginator(blogs_and_photos, 6)
    
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'blog/home.html')



def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})
    

def logout_user(request):
    logout(request)
    return redirect('/')



def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})

@login_required
def all_profile(request):
    users = User.objects.all().exclude(is_superuser=True)
    return render(request, 'authentication/all_profile.html',  {'users': users})

@login_required
def view_profile(request, user_id):
    # Récupérer l'utilisateur à partir de l'ID dans l'URL
    user = get_object_or_404(User, id=user_id)
    # Filtrer les comics possédés par l'utilisateur
    comics = Comics.objects.filter(author=user, posseded=True) | Comics.objects.filter(author=user, want=True)

    context = {'user': user, 'comics': comics}
    return render(request, 'authentication/view_profile.html', context)




@login_required
def remove_comics(request, comics_id):
    comics = get_object_or_404(Comics, id=comics_id)
    request.user.comics_set.remove(comics)
    request.user.want_set.remove(comics)
    return redirect('profile')