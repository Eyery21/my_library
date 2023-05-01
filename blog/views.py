from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render, get_object_or_404
from blog.forms import PhotoForm, SearchForm, ComicForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import DeleteBlogForm, ComicsModif
from .models import Comics
from . import forms, models


from django.views.generic import ListView
from django.db.models import Q
from .models import Blog, Comics, SeriesComics

from django.views.generic import ListView


@login_required
@permission_required('blog.add_photo', raise_exception=True)
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



#### page d'accuile ####

def base(request):
    
    return render(request, 'base.html')

def home(request):
    query = request.GET.get('query')
    comics = Comics.objects.order_by('title')
    paginator = Paginator(comics, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'form': SearchForm(initial={'query': query})}
    return render(request, 'blog/home.html', context)


def blog_search(request):
    try:
        query = request.GET.get('query')
        comics = []
        if query:
            # Recherche les comics dont le titre ou le contenu contient la chaîne de recherche
            comics = Comics.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        context = {'comics': comics, 'form': SearchForm(initial={'query': query})}
    except Exception as e:
        context = {'error': str(e)}

    return render(request, 'blog/home.html', context)



@login_required
def blog_and_photo_upload(request):
    # blog_form = forms.BlogForm()
    comic_form = forms.ComicForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        # blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        comic_form = forms.ComicForm(request.POST, request.FILES)
        if all([comic_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            # blog = blog_form.save(commit=False)
            # blog.author = request.user
            # blog.photo = photo
            # blog.save()
            comic = comic_form.save(commit=False)
            comic.author = request.user
            comic.photo = photo
            comic.save()

            return redirect('home')
    context = {
        'comic_form': comic_form,
        'photo_form': photo_form,

    }
    return render(request, 'blog/create_blog_post.html', context=context)



#### CRUD BLOG ####

@login_required
def update(request, comics_id):
    comics = get_object_or_404(Comics, id=comics_id)
    
    # Vérifier que l'utilisateur connecté est l'auteur de la bande dessinée
    if request.user != comics.author:
        messages.warning(request, 'You are not allowed to edit this comics')
        return redirect('view_comics', comics_id=comics.id)

    if request.method == 'POST':
        form = ComicsModif(request.POST, request.FILES, instance=comics)
        if form.is_valid():
            form.save()
            return redirect('view_comics', comics_id=comics.id)
    else:
        form = ComicsModif(instance=comics)
        
    context = {'form': form, 'comics': comics}
    return render(request, 'blog/update.html', context=context)




def delete(request, comics_id):
    comics = get_object_or_404(Comics, id=comics_id)
    if request.user == comics.author:

        if request.method == 'POST':
            form = DeleteBlogForm(request.POST)
            if form.is_valid():
                comics.delete()
                return HttpResponseRedirect('/home')
        else:
            form = DeleteBlogForm(initial={'comics_id': comics_id})
        context = {'delete_form': form}
    return render(request, 'blog/edit_blog.html', context=context)




@login_required
def view_blog(request, comics_id):
    comics = get_object_or_404(models.Comics, id=comics_id)
    return render(request, 'blog/view_blog.html', {'comics': comics})


#### SEARCH ####
@login_required
def one_shot(request):
    comics = Comics.objects.all().filter(one_shot=True)
    return render(request, 'blog/search/one_shot.html', {'comics': comics})

@login_required
def list_series_comics(request):
    comics = SeriesComics.objects.filter(one_shot=False, first_comics=True)
    return render(request, 'blog/search/series_comics.html', {'comics': comics})   

def category_rebirth(request):
    comics = Comics.objects.filter(category='Rebirth').order_by('id')
    return render(request, 'blog/search/rebirth.html', {'comics': comics})

def category_52(request):
    comics = Comics.objects.filter(category='New 52').order_by('title')
    return render(request, 'blog/search/New_52.html', {'comics': comics})

def category_heros(request):
    comics = Comics.objects.filter(hero='Superman').order_by('title')
    return render(request, 'blog/search/Superman.html', {'comics': comics})

#modifie et suprrime un post avec un formulaire


@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})



