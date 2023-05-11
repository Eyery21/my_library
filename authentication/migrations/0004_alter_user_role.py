# Generated by Django 4.1.7 on 2023-05-06 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Createur'), ('SUBSCRIBER', ' Abonné'), ('USER    ', 'User')], max_length=30),
        ),
    ]