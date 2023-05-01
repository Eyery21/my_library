# Generated by Django 4.1.7 on 2023-04-30 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comics_author_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('comics_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.comics')),
                ('category', models.CharField(default='Other', max_length=50)),
            ],
            bases=('blog.comics',),
        ),
    ]
