from django.urls import path, include
from .views import index_view, register_view, logout_view

urlpatterns = [
    path('', index_view, name='index'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
