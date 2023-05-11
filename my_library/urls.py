
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import blog.views
from blog.models import Blog

from blog.views import blog_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', authentication.views.signup_page, name='signup'),# s'inscrire
    path('login/', authentication.views.login_page, name='login'),# se connecter
    path('logout', authentication.views.logout_user, name='logout'),# se déconnecter

    path('', blog.views.base, name='base' ),
    path('home/', blog.views.home, name='home'),# si ont est connecter
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),# page pour ajouter une photo de profile
    path('profile-photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),# page pour changer photo de profile

    path('profile/', blog.views.view_profile, name='profile'),
    path('remove_comics/<int:comics_id>', authentication.views.remove_comics, name='remove_comics'),
    path('all_profile/', authentication.views.all_profile, name='all_profile'),
    path('view_profile/<int:user_id>', authentication.views.view_profile, name='view_profile'),



    path('blog/create', blog.views.blog_and_photo_upload, name='blog_create'),
    
    # path('blog/multiple_create', blog.views.multiple_create, name='multiple_create'),

    path('blog/<int:comics_id>', blog.views.view_blog, name='view_comics'),

    path('blog/one_shot/', blog.views.one_shot, name='one_shot'),

    path('blog/Posseded/', blog.views.posseded, name='posseded'),
    path('blog/Want/', blog.views.want, name='want'),
    path('blog/series_comics/', blog.views.list_series_comics, name='series_comics'),
    path('blog/rebirth/', blog.views.category_rebirth, name='rebirth'),
    path('blog/New_52/', blog.views.category_52, name='New 52'),
    path('blog/Superman/', blog.views.category_heros, name='Superman'),
    path('blog/Black_Label', blog.views.category_BL, name='BL'),

    
    path('blog/<int:comics_id>/update', blog.views.update, name='update_blog'),

    path('blog/<int:comics_id>/edit', blog.views.delete, name='edit_blog'),
    path('search/', blog.views.blog_search, name='search'),




    path('follow-users/', blog.views.follow_users, name='follow_users'), #formulaire pour suivre un utilisateur

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
