from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Comics

# Create your models here.


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ADMIN = 'ADMIN'
    USER = 'USER    '

    # ROLE_CHOICES = (
    #     (CREATOR, 'Createur'),
    #     (SUBSCRIBER, ' Abonné'),
    #     (USER, 'User')
    # )
    POSSESSED = 'posseded'
    WANT = 'want'
    CATEGORY_CHOICES = (
        (POSSESSED, 'Possédées'),
        (WANT, 'Want'),
    )

    profile_photo = models.ImageField(verbose_name='photo de profil')
    # role = models.CharField(max_length=30, choices=ROLE_CHOICES)


    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    want_set = models.ManyToManyField(
        Comics,
        related_name='want_users',
        blank=True,
        verbose_name='envie de lecture',
    )