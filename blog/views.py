from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render, get_object_or_404
from blog.forms import PhotoForm
from django.core.paginator import Paginator


from . import forms, models


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


# @login_required
# def home(request):
#     photos = models.Photo.objects.all()
#     return render(request, 'blog/home.html', context={'photos': photos})


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

@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.photo = photo
            blog.save()
            blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
        }
    return render(request, 'blog/create_blog_post.html', context=context)


@login_required
def home(request):
    photos = models.Photo.objects.all().order_by('-id')
    blogs_list = models.Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs_list, 4) # paginer avec 4 éléments par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'photos': photos, 'page_obj': page_obj})


    
@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', {'blog': blog})


#modifie et suprrime un post avec un formulaire
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
                if 'delete_blog' in request.POST:
                    delete_form = forms.DeleteBlogForm(request.POST)
                    if delete_form.is_valid():
                        blog.delete()
                        return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
}
    return render(request, 'blog/edit_blog.html', context=context)



@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/follow_users_form.html', context={'form': form})