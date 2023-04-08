
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', authentication.views.signup_page, name='signup'),# s'inscrire
    path('login/', authentication.views.login_page, name='login'),# se connecter
    path('logout', authentication.views.logout_user, name='logout'),# se déconnecter

    path('home/', blog.views.home, name='home'),# si ont est connecter
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),# page pour ajouter une photo de profile
    path('profile-photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),# page pour changer photo de profile

    path('blog/create', blog.views.blog_and_photo_upload, name='blog_create'),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
