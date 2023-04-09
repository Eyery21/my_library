from django import forms
from . import models
from django.contrib.auth import get_user_model



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


        
class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)



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