from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from .forms import SGI_AuthenticationForm

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('auth/login/', LoginView.as_view(authentication_form=SGI_AuthenticationForm), name='login'),

    path('auth/', include('django.contrib.auth.urls')),
]
