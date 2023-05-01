from django import forms
from . import models
from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import CheckboxInput
from .models import SeriesComics, Characters, Comics
from django.forms import modelform_factory



class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['images', 'caption']


class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['images', 'caption']



class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'content']

class ComicForm(forms.ModelForm):
    one_shot = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'form-check-input'}))

    category = forms.CharField(max_length=50, required=True, widget=forms.Select(choices=[
        ('Rebirth', 'Rebirth'),
        ('New 52', 'New 52'), 
        ('Pre-Crisis', 'Pre-Crisis'),
    ]))

    hero = forms.CharField(max_length=50, required=True, widget=forms.Select(choices=[
        ('Batman', 'Batman'),
        ('Superman', 'Superman'), 
    ]))

    class Meta:
        model = Comics
        fields = ['title', 'content', 'one_shot', 'first_comics', 'category', 'hero']


class ComicsModif(forms.ModelForm):
    class Meta:
        model = Comics
        fields = ['title', 'content', 'one_shot', 'first_comics', 'category', 'hero']

class DeleteBlogForm(forms.Form):
    comics_id = forms.IntegerField(widget=forms.HiddenInput)



User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']

    
class SearchForm(forms.Form):
    
    query = forms.CharField(
        label='Recherche',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Rechercher...',
            'id': 'search-query',
            'name': 'query'
        })
    )