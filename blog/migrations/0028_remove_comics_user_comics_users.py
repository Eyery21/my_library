# Generated by Django 4.1.7 on 2023-05-06 15:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0027_comics_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comics',
            name='user',
        ),
        migrations.AddField(
            model_name='comics',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]