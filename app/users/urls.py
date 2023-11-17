from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('reg/', views.UserCreateView.as_view(), name='reg'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
