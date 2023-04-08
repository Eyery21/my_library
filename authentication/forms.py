# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

#### formulaire d'inscription en utilisant le package en ligne UserCreationForm ####
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'role']




class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )
