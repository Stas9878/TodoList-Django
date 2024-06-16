from django.urls import path
from .views import user_profile


app_name = 'user_profile'

urlpatterns = [
    path('<str:username>/', user_profile, name='user_profile'),
]
