# Generated by Django 4.1.7 on 2023-05-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_follows_alter_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Createur'), ('SUBSCRIBER', ' Abonné'), ('ADMIN', 'Admin'), ('USER    ', 'User')], max_length=30),
        ),
    ]
