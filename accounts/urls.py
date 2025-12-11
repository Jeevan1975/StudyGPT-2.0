from django.urls import path
from django.contrib.auth import views as auth_view
from .import views

app_name = 'accounts'

urlpatterns = [
    path(
        'register/',
        views.register_view,
        name='register'
    ),
    
    path(
        'login/',
        views.login_view,
        name='login'
    ),
    
    path(
        'logout/',
        auth_view.LogoutView.as_view(
            next_page='accounts:login'
        ),
        name='logout'
    ),
]
