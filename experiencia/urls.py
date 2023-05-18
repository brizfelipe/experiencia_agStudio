from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'experiencia'  # define o namespace para o aplicativo

urlpatterns = [
    path('form',views.form,name='form'),
]