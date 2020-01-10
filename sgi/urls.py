from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from .forms import SGIAuthenticationForm

urlpatterns = [

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            form_class=SGIAuthenticationForm
        ),
        name='login'
    ),

    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),

    path(
        '',
        include('sgi.home.urls')
    ),

    path(
        'base/',
        include('sgi.base.urls')
    ),

    path(
        'academico/',
        include('sgi.academico.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),
]
