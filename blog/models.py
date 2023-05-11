from django.db import models
from django.conf import settings
from PIL import Image
from django.contrib.auth import get_user_model



# Create your models here.


class Photo(models.Model):
    images = models.ImageField(verbose_name='image')
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_ceated = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)

class Blog(models.Model):
    photo = models.ForeignKey(
        Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
contributors = models.ManyToManyField(
settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')

class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)
    
    class Meta:
        unique_together = ('contributor', 'blog')


class Comics(models.Model):
    photo = models.ForeignKey(
        Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    one_shot = models.BooleanField(default=False)
    first_comics = models.BooleanField(default=False)
    author = models.CharField(max_length=128)
    category = models.CharField(max_length=50, default='Other')
    hero = models.CharField(max_length=50, default='Other')
    posseded = models.BooleanField(default=False)
    want = models.BooleanField(default=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)



    def __str__(self):
        return f'{self.title}'

class SeriesComics(Comics):
    pass
class Characters(Comics):
    pass



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title



