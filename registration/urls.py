from django.urls import path
from . import views


urlpatterns = [
    path('register', views.registration, name='registration'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
]
